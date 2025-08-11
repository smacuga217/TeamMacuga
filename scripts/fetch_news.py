#!/usr/bin/env python3
import json, re, time
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
MAX_PER_QUERY = 8          # keep page light
TIMEOUT = 8
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; TeamMacugaBot/1.0)"}
OUTFILE = "_data/news.json"

GOOGLE_HOSTS = ("news.google.", "googleusercontent.com", "gstatic.com")

def original_link(google_link: str) -> str:
    """Google News links often contain ?url=<real-url> — extract it."""
    try:
        u = urlparse(google_link)
        if "news.google." in u.netloc:
            qs = parse_qs(u.query)
            if "url" in qs and qs["url"]:
                return unquote(qs["url"][0])
        return google_link
    except Exception:
        return google_link

def fetch_og_meta(url: str) -> tuple[str | None, datetime | None]:
    """Return (image_url, published_dt) from the article page, if available."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

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
            'time[datetime]'
        ]:
            t = soup.select_one(sel)
            dt = t.get("content") if t else None
            if not dt and t and t.has_attr("datetime"):
                dt = t["datetime"]
            if dt:
                try:
                    # Normalize to aware UTC
                    published = datetime.fromisoformat(dt.replace("Z","+00:00")).astimezone(timezone.utc)
                    break
                except Exception:
                    pass

        return img, published
    except Exception:
        return None, None

def to_iso(d: datetime | None, fallback_struct) -> str:
    if isinstance(d, datetime):
        return d.astimezone(timezone.utc).isoformat()
    # fallback from feedparser’s struct_time
    try:
        return datetime(*fallback_struct[:6], tzinfo=timezone.utc).isoformat()
    except Exception:
        return datetime.now(timezone.utc).isoformat()

def is_google_img(url: str | None) -> bool:
    if not url: return False
    host = urlparse(url).netloc.lower()
    return any(h in host for h in GOOGLE_HOSTS)

def fetch_query(q: str):
    url = f"https://news.google.com/rss/search?q={requests.utils.quote(q)}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:MAX_PER_QUERY]:
        link = original_link(entry.link)
        source = entry.get("source", {}).get("title") or entry.get("source_title") or ""
        # fetch OG image + better published
        og_image, og_published = fetch_og_meta(link)

        published_iso = to_iso(og_published, entry.get("published_parsed") or entry.get("updated_parsed"))
        # If OG image is a Google image, drop it (we’ll hide in UI)
        if is_google_img(og_image):
            og_image = None

        items.append({
            "title": entry.title,
            "link": link,
            "source": source.strip() or urlparse(link).netloc,
            "published": published_iso,       # ISO string for sorting in Jekyll
            "image": og_image or "",          # may be empty
        })
        time.sleep(0.25)  # be polite
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

    # newest first before writing (Jekyll will also sort)
    deduped.sort(key=lambda x: x["published"], reverse=True)

    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(deduped, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
