#!/usr/bin/env python3
import json, time
from datetime import datetime, timezone
from urllib.parse import urlparse, parse_qs, unquote

import requests
import feedparser
from bs4 import BeautifulSoup

# ----------------------------------
# Config
# ----------------------------------
QUERIES = [
    "Macuga ski",
    "Team Macuga ski",
    "Lauren Macuga ski",
    "Sam Macuga ski",
    "Alli Macuga ski",
    "Daniel Macuga ski",
]
MAX_PER_QUERY = 20
TIMEOUT = 10
HEADERS = {"User-Agent": "TeamMacugaBot/1.0 (+https://teammacuga.com)"}
OUTFILE = "_data/news_feed.json"

GOOGLE_HOSTS = ("news.google.", "googleusercontent.com", "gstatic.com")

def original_link(google_link: str) -> str:
    try:
        u = urlparse(google_link)
        if "news.google." in u.netloc:
            qs = parse_qs(u.query)
            if qs.get("url"):
                return unquote(qs["url"][0])
        return google_link
    except Exception:
        return google_link

def pick_parser() -> str:
    # Try lxml if installed, otherwise built-in html.parser
    try:
        import lxml  # noqa
        return "lxml"
    except Exception:
        return "html.parser"

PARSER = pick_parser()

def fetch_og_meta(url: str):
    """Return (image_url, published_dt | None) from the article page."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, PARSER)

        # og:image or twitter:image
        img = None
        for sel in [
            'meta[property="og:image"]',
            'meta[name="og:image"]',
            'meta[name="twitter:image"]',
            'meta[property="twitter:image"]',
        ]:
            tag = soup.select_one(sel)
            if tag and tag.get("content"):
                img = tag["content"].strip()
                break

        # published time
        published = None
        for sel in [
            'meta[property="article:published_time"]',
            'meta[name="article:published_time"]',
            'meta[itemprop="datePublished"]',
            'time[datetime]',
        ]:
            t = soup.select_one(sel)
            dt = (t.get("content") if t else None) or (t.get("datetime") if t and t.has_attr("datetime") else None)
            if dt:
                try:
                    # normalize common formats
                    if dt.endswith("Z"):  # ISO Z
                        published = datetime.fromisoformat(dt.replace("Z", "+00:00"))
                    else:
                        published = datetime.fromisoformat(dt)
                    published = published.astimezone(timezone.utc)
                    break
                except Exception:
                    # last resort: forget it
                    pass

        return img, published
    except Exception:
        return None, None

def to_iso(d, fallback_struct):
    if isinstance(d, datetime):
        return d.astimezone(timezone.utc).isoformat()
    try:
        return datetime(*fallback_struct[:6], tzinfo=timezone.utc).isoformat()
    except Exception:
        return datetime.now(timezone.utc).isoformat()

def is_google_img(url: str | None) -> bool:
    if not url:
        return False
    host = urlparse(url).netloc.lower()
    return any(h in host for h in GOOGLE_HOSTS)

def fetch_query(q: str):
    # Fetch RSS with requests (adds UA + timeout), then parse
    rss_url = (
        "https://news.google.com/rss/search?"
        f"q={requests.utils.quote(q)}&hl=en-US&gl=US&ceid=US:en"
    )
    items = []
    try:
        resp = requests.get(rss_url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except Exception:
        return items

    for entry in feed.entries[:MAX_PER_QUERY]:
        link = original_link(entry.link)
        source = (entry.get("source", {}) or {}).get("title") or entry.get("source_title") or ""
        og_image, og_published = fetch_og_meta(link)
        published_iso = to_iso(og_published, entry.get("published_parsed") or entry.get("updated_parsed"))

        if is_google_img(og_image):
            og_image = None

        items.append({
            "title": entry.title,
            "link": link,
            "source": (source or urlparse(link).netloc).strip(),
            "published": published_iso,
            "image": og_image or "",
        })
        time.sleep(0.25)  # polite
    return items

def main():
    all_items = []
    for q in QUERIES:
        all_items.extend(fetch_query(q))

    # de-dup by (title, link)
    seen = set()
    deduped = []
    for it in all_items:
        key = (it["title"], it["link"])
        if key not in seen:
            seen.add(key)
            deduped.append(it)

    deduped.sort(key=lambda x: x["published"], reverse=True)

    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(deduped, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
