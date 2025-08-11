# scripts/fetch_news.py
import feedparser, requests, time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urlparse
import json, pathlib

QUERIES = [
    "Macuga ski", "Team Macuga ski",
    "Lauren Macuga ski", "Sam Macuga ski",
    "Alli Macuga ski", "Daniel Macuga ski"
]
MAX_PER_QUERY = 12
UA = {"User-Agent":"Mozilla/5.0 (compatible; TeamMacugaNews/1.0)"}

def pick_image(url:str)->str|None:
    try:
        r = requests.get(url, timeout=8, headers=UA)
        if r.status_code >= 400: return None
        soup = BeautifulSoup(r.text, "lxml")
        for sel, attr in [
            ('meta[property="og:image"]', "content"),
            ('meta[name="twitter:image"]', "content"),
            ('link[rel="image_src"]', "href"),
        ]:
            tag = soup.select_one(sel)
            if tag:
                src = tag.get(attr)
                if src and src.startswith("//"): src = "https:" + src
                return src
    except Exception:
        return None

items = []
for q in QUERIES:
    feed = f"https://news.google.com/rss/search?q={quote_plus(q)}&hl=en-US&gl=US&ceid=US:en"
    d = feedparser.parse(feed)
    for e in d.entries[:MAX_PER_QUERY]:
        link = e.link
        ts = int(time.mktime(e.published_parsed)) if getattr(e, "published_parsed", None) else 0
        date_str = time.strftime("%Y-%m-%d", e.published_parsed) if ts else None

        # try RSS media first
        img = None
        if "media_thumbnail" in e: img = e.media_thumbnail[0].get("url")
        if not img and "media_content" in e: img = e.media_content[0].get("url")
        if not img: img = pick_image(link)

        source = getattr(getattr(e, "source", None), "title", None) or urlparse(link).netloc.replace("www.","")

        items.append({
            "title": e.title,
            "link": link,
            "source": source,
            "date": date_str,
            "ts": ts,
            "image": img
        })

# de-dupe by link
seen = set(); deduped = []
for it in items:
    if it["link"] in seen: continue
    seen.add(it["link"]); deduped.append(it)

# newest first
deduped.sort(key=lambda x: x.get("ts", 0), reverse=True)

pathlib.Path("_data").mkdir(exist_ok=True)
with open("_data/news.json","w") as f:
    json.dump(deduped, f, indent=2)
print(f"Wrote {_data := 'news.json'} with", len(deduped), "items")
