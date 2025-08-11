# scripts/fetch_news.py
import json, time, re, sys
from datetime import datetime, timezone
from urllib.parse import urlparse, urljoin

import feedparser
import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateparse

OUTFILE = "_data/news.json"

# Search terms (you gave these)
KEYWORDS = [
    "Macuga", "Team Macuga", "Lauren Macuga",
    "Sam Macuga", "Alli Macuga", "Daniel Macuga",
]

# Require "ski" in the article (title/summary) in addition to a keyword
REQUIRE_TERM = "ski"

# How many items per query to collect (RSS feeds return ~10-50)
MAX_PER_QUERY = 20

# User-Agent so publishers serve full pages
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)

session = requests.Session()
session.headers.update({"User-Agent": UA})


def google_news_rss(query: str) -> str:
    # hl=en for English; gl=US geo; ceid=US:en
    return f"https://news.google.com/rss/search?q={requests.utils.quote(query)}&hl=en-US&gl=US&ceid=US:en"


def is_bad_image(url: str) -> bool:
    if not url:
        return True
    u = url.lower()
    bad_bits = ["google", "gstatic", "favicon", ".ico", "sprite", "logo", "placeholder"]
    return any(b in u for b in bad_bits)


def absolutize(src: str, base: str) -> str:
    if not src:
        return ""
    return urljoin(base, src)


def extract_meta_image_and_date(html_url: str) -> tuple[str, str]:
    """
    Returns (image_url, iso_date or ""), both may be "" if not found.
    """
    try:
        # 1) follow Google News redirect to publisher
        r = session.get(html_url, timeout=15, allow_redirects=True)
        r.raise_for_status()
        final_url = r.url

        soup = BeautifulSoup(r.text, "html.parser")

        # Candidate image tags (priority order)
        candidates = [
            ('meta[property="og:image"]', "content"),
            ('meta[name="og:image"]', "content"),
            ('meta[name="twitter:image:src"]', "content"),
            ('meta[name="twitter:image"]', "content"),
            ('meta[property="twitter:image"]', "content"),
            ("link[rel='image_src']", "href"),
        ]

        img_url = ""
        for selector, attr in candidates:
            tag = soup.select_one(selector)
            if tag:
                candidate = absolutize(tag.get(attr) or "", final_url)
                if candidate and not is_bad_image(candidate):
                    img_url = candidate
                    break

        # Candidate publish date tags
        date_selectors = [
            ('meta[property="article:published_time"]', "content"),
            ('meta[name="article:published_time"]', "content"),
            ('meta[name="pubdate"]', "content"),
            ('meta[name="publish-date"]', "content"),
            ('meta[name="date"]', "content"),
            ('meta[itemprop="datePublished"]', "content"),
            ('time[datetime]', "datetime"),
        ]

        iso_date = ""
        for selector, attr in date_selectors:
            t = soup.select_one(selector)
            if t:
                raw = (t.get(attr) or "").strip()
                if raw:
                    try:
                        dt = dateparse.parse(raw)
                        if not dt.tzinfo:
                            dt = dt.replace(tzinfo=timezone.utc)
                        iso_date = dt.astimezone(timezone.utc).isoformat()
                        break
                    except Exception:
                        pass

        return img_url, iso_date
    except Exception:
        return "", ""


def entry_date(entry) -> datetime:
    # Prefer publisher date we’ll scrape later; otherwise RSS
    for key in ("published", "updated"):
        if getattr(entry, key, None):
            try:
                return dateparse.parse(getattr(entry, key)).astimezone(timezone.utc)
            except Exception:
                pass
    # Try structured *_parsed from feedparser
    for key in ("published_parsed", "updated_parsed"):
        val = getattr(entry, key, None)
        if val:
            try:
                return datetime(*val[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return datetime.now(timezone.utc)


def normalize_source(link: str) -> str:
    try:
        host = urlparse(link).netloc
        if host.startswith("www."):
            host = host[4:]
        if host.startswith("news.google."):
            return "Google News"
        return host
    except Exception:
        return "News"


def fetch():
    items = []

    for kw in KEYWORDS:
        feed_url = google_news_rss(kw)
        feed = feedparser.parse(feed_url)
        for e in feed.entries[:MAX_PER_QUERY]:
            title = (e.title or "").strip()
            summary = (getattr(e, "summary", "") or "")
            link = (e.link or "")

            blob = f"{title} {summary}".lower()
            if REQUIRE_TERM not in blob:
                # must include "ski"
                continue
            if not any(k.lower() in blob for k in [kw.lower()] + [x.lower() for x in KEYWORDS]):
                continue

            # Resolve to publisher + extract OG image/date
            img, better_iso = extract_meta_image_and_date(link)
            # Fallback to RSS date if OG date missing
            dt = dateparse.parse(better_iso).astimezone(timezone.utc) if better_iso else entry_date(e)

            items.append({
                "title": title,
                "link": link,
                "date": dt.isoformat(),
                "source": normalize_source(link),
                "image": "" if is_bad_image(img) else img
            })

            time.sleep(0.5)  # be nice

    # De-dupe by title+source (simple)
    seen = set()
    deduped = []
    for it in sorted(items, key=lambda x: x["date"], reverse=True):
        key = (it["title"].lower(), it["source"].lower())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(it)

    # Write JSON
    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(deduped, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(deduped)} items -> {OUTFILE}")


if __name__ == "__main__":
    try:
        fetch()
    except KeyboardInterrupt:
        sys.exit(1)
