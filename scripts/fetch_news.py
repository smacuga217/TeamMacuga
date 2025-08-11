#!/usr/bin/env python3
import json, time, re, urllib.parse, requests
from pathlib import Path
import feedparser

# -------- settings ----------
TERMS = [
  "Macuga", "Team Macuga", "Lauren Macuga", "Sam Macuga", "Alli Macuga", "Daniel Macuga"
]
# Require 'ski' context (common variations)
SKI_RE = re.compile(r"\bski(?:ing|er|-?jump|)\b|mogul|alpine|slalom|downhill|super[- ]?g", re.I)
MAX_ITEMS = 40   # keep the data file lean
USER_AGENT = "TeamMacugaBot/1.0 (+https://teammacuga.com)"
OUT = Path("_data/news.json")
# ----------------------------

session = requests.Session()
session.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})

def google_news_feed(term: str) -> str:
    q = f'{term} AND (ski OR skiing OR skier OR moguls OR alpine OR slalom OR downhill OR "super g" OR "ski jumping")'
    # you can add recency hint: when:365d if you want fresher bias
    qs = urllib.parse.urlencode({"q": q, "hl":"en-US", "gl":"US", "ceid":"US:en"})
    return f"https://news.google.com/rss/search?{qs}"

def pick_image(entry, fallback_url: str | None):
    # 1) media:content on the feed
    media = getattr(entry, "media_content", None)
    if media and isinstance(media, list):
        url = media[0].get("url")
        if url: return url

    # 2) Try og:image from the article page
    if not fallback_url: return None
    try:
        r = session.get(fallback_url, timeout=8)
        if r.ok:
            html = r.text
            # prefer og:image
            m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if m: return m.group(1)
            # or twitter:image
            m = re.search(r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
            if m: return m.group(1)
    except requests.RequestException:
        pass
    return None

def normalize_link(link: str):
    # Some Google News links wrap publisher URLs. Try to unwrap ?url= param if present.
    try:
        u = urllib.parse.urlparse(link)
        qs = urllib.parse.parse_qs(u.query)
        if "url" in qs and qs["url"]:
            return qs["url"][0]
    except Exception:
        pass
    return link

seen = set()
items = []

for term in TERMS:
    feed_url = google_news_feed(term)
    feed = feedparser.parse(feed_url)

    for e in feed.entries:
        title = e.title.strip()
        if not SKI_RE.search(title + " " + getattr(e, "summary", "")):
            continue

        link = normalize_link(e.link)
        key = (title.lower(), link)
        if key in seen: 
            continue
        seen.add(key)

        # date → ISO string
        # feedparser gives e.published_parsed sometimes
        ts = None
        if getattr(e, "published_parsed", None):
            ts = int(time.mktime(e.published_parsed))
        elif getattr(e, "updated_parsed", None):
            ts = int(time.mktime(e.updated_parsed))
        if not ts:
            # if missing, skip (keeps sorting reliable)
            continue

        date_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))
        source = getattr(getattr(e, "source", None), "title", None) or getattr(e, "publisher", None) or ""

        image = pick_image(e, link)

        items.append({
            "title": title,
            "link": link,
            "source": source,
            "date": date_iso,
            "image": image
        })

# sort newest first, trim
items.sort(key=lambda x: x["date"], reverse=True)
items = items[:MAX_ITEMS]

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(items, indent=2))
print(f"Wrote {len(items)} items to {OUT}")
