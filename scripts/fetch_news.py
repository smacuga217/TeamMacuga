# scripts/fetch_news.py
import json, html, pathlib, time
import requests, feedparser
from bs4 import BeautifulSoup as BS

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"
DATA.mkdir(exist_ok=True)

QUERIES = [
  'https://news.google.com/rss/search?q=Macuga&hl=en-US&gl=US&ceid=US:en',
  'https://news.google.com/rss/search?q="Team+Macuga"&hl=en-US&gl=US&ceid=US:en',
  'https://news.google.com/rss/search?q="Lauren+Macuga"&hl=en-US&gl=US&ceid=US:en',
  'https://news.google.com/rss/search?q="Sam+Macuga"&hl=en-US&gl=US&ceid=US:en',
  'https://news.google.com/rss/search?q="Alli+Macuga"&hl=en-US&gl=US&ceid=US:en',
  'https://news.google.com/rss/search?q="Daniel+Macuga"&hl=en-US&gl=US&ceid=US:en',
]

UA = {"User-Agent": "TeamMacugaBot/1.0 (+github actions)"}

def og_image(url):
    try:
        h = requests.get(url, headers=UA, timeout=12).text
        s = BS(h, "lxml")
        for sel in ['meta[property="og:image"]', 'meta[name="twitter:image"]']:
            m = s.select_one(sel)
            if m and m.get("content"):
                return m["content"]
    except:
        return None

seen = set()
items = []
for q in QUERIES:
    feed = feedparser.parse(q)
    for e in feed.entries[:12]:
        link = e.link
        if link in seen: 
            continue
        seen.add(link)
        itm = {
            "title": html.unescape(e.title),
            "link": link,
            "source": getattr(e, "source", {}).get("title", "") or getattr(e, "author", ""),
            "date": getattr(e, "published", ""),
            "image": None
        }
        items.append(itm)

# Resolve images (best-effort)
for it in items[:16]:
    it["image"] = og_image(it["link"])
    time.sleep(0.5)

(DATA / "news.json").write_text(json.dumps(items, indent=2))
print("Wrote _data/news.json")
