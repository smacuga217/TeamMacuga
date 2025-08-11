#!/usr/bin/env python3
"""
Fetch Team Macuga news into _data/news.json

Requires:
  pip install feedparser requests beautifulsoup4 lxml python-dateutil

Run:
  python scripts/fetch_news.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse, parse_qs, urljoin, unquote

import feedparser  # type: ignore
import requests
from bs4 import BeautifulSoup  # type: ignore
from dateutil import parser as dtparse  # type: ignore


# ---------- Settings ----------
QUERIES: List[str] = [
    "Macuga",
    "Team Macuga",
    "Lauren Macuga",
    "Sam Macuga",
    "Alli Macuga",
    "Daniel Macuga",
]

GOOGLE_RSS = "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
TIMEOUT = 12  # seconds for HTTP requests
MAX_PER_QUERY = 12
MAX_TOTAL = 60

# keep items that contain 'ski' or variants in title/summary
SKI_RE = re.compile(r"\bski\w*\b", re.IGNORECASE)

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
)
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA})


# ---------- Paths ----------
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "_data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "news.json"


# ---------- Helpers ----------
def parse_date(entry) -> Optional[datetime]:
    """Return timezone-aware UTC datetime if possible."""
    for key in ("published", "updated", "pubDate"):
        val = entry.get(key) or entry.get(f"{key}_parsed")
        if not val:
            continue
        try:
            if isinstance(val, str):
                dt = dtparse.parse(val)
            else:
                # time.struct_time from feedparser
                dt = datetime(*val[:6])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            else:
                dt = dt.astimezone(timezone.utc)
            return dt
        except Exception:
            continue
    return None


def canonical_link(link: str) -> str:
    """Normalize links and unwrap Google News redirects (keep original URL)."""
    try:
        p = urlparse(link)
        if "news.google." in p.netloc:
            qs = parse_qs(p.query)
            if "url" in qs and qs["url"]:
                return unquote(qs["url"][0])
        # strip tracking params commonly used
        clean_qs = []
        if p.query:
            for k, v in parse_qs(p.query, keep_blank_values=True).items():
                if k.lower().startswith(("utm_", "gclid", "fbclid", "mc_cid", "mc_eid")):
                    continue
                for item in v:
                    clean_qs.append(f"{k}={item}")
        q = "&".join(clean_qs)
        return p._replace(query=q).geturl()
    except Exception:
        return link


def source_from_link(link: str) -> str:
    try:
        host = urlparse(link).netloc
        if host.startswith("www."):
            host = host[4:]
        return host
    except Exception:
        return "source"


def entry_image(entry, page_url: str) -> Optional[str]:
    """Try RSS media first, then scrape OpenGraph/Twitter image."""
    # RSS media hints
    media = entry.get("media_content") or entry.get("media_thumbnail")
    if media and isinstance(media, list):
        for m in media:
            url = m.get("url")
            if url:
                return url

    # Some feeds tuck images under links
    if "links" in entry:
        for l in entry["links"]:
            if l.get("type", "").startswith("image") and l.get("href"):
                return l["href"]

    # Fetch page and read OG tags
    try:
        r = SESSION.get(page_url, timeout=TIMEOUT)
        if not (200 <= r.status_code < 400):
            return None
        html = r.text
        soup = BeautifulSoup(html, "lxml")

        # Prefer og:image
        og = soup.find("meta", property="og:image") or soup.find("meta", attrs={"name": "og:image"})
        if og and og.get("content"):
            return urljoin(page_url, og["content"])

        tw = soup.find("meta", property="twitter:image") or soup.find("meta", attrs={"name": "twitter:image"})
        if tw and tw.get("content"):
            return urljoin(page_url, tw["content"])

        # Fallback: first <img> with reasonable size
        img = soup.find("img", src=True)
        if img:
            return urljoin(page_url, img["src"])
    except Exception:
        return None

    return None


def keep_item(entry) -> bool:
    """Filter: must mention 'ski' somewhere (title/summary)."""
    text = " ".join(
        [
            entry.get("title", ""),
            entry.get("summary", ""),
            entry.get("description", ""),
        ]
    )
    return bool(SKI_RE.search(text))


# ---------- Main ----------
def fetch_query(q: str) -> List[Dict]:
    url = GOOGLE_RSS.format(q=requests.utils.quote(q))
    feed = feedparser.parse(url)
    items: List[Dict] = []

    for e in feed.entries[:MAX_PER_QUERY]:
        if not keep_item(e):
            continue

        link = canonical_link(e.get("link", ""))
        title = e.get("title", "").strip()
        date = parse_date(e) or datetime.now(timezone.utc)

        img = entry_image(e, link)

        items.append(
            {
                "title": title,
                "link": link,
                "source": e.get("source", {}).get("title") or source_from_link(link),
                "date": date.isoformat(),  # ISO string; Jekyll can format with | date
                "image": img,
            }
        )
    return items


def main() -> int:
    all_items: List[Dict] = []
    seen = set()

    for q in QUERIES:
        try:
            items = fetch_query(q)
        except Exception as ex:
            print(f"[warn] query '{q}': {ex}", file=sys.stderr)
            continue

        for it in items:
            key = (it["title"].lower(), it["link"])
            if key in seen:
                continue
            seen.add(key)
            all_items.append(it)

    # Sort newest → oldest and cap list
    all_items.sort(key=lambda x: x["date"], reverse=True)
    if len(all_items) > MAX_TOTAL:
        all_items = all_items[:MAX_TOTAL]

    # Write
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)

    print(f"[ok] wrote {OUT_PATH} ({len(all_items)} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
