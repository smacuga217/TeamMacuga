import sys, yaml, re, os, datetime as dt
from urllib.request import urlopen, Request
from html.parser import HTMLParser

ATHLETES = [
  ("Lauren Macuga","Super-G","https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=228398"),
  ("Alli Macuga","Moguls","https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=FS&competitorid=220306"),
  ("Sam Macuga","Ski Jumping","https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid=211435"),
  ("Daniel Macuga","Alpine","https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=260517"),
]

class TextGrab(HTMLParser):
    def __init__(self): super().__init__(); self.text=[]
    def handle_data(self, d): 
        d=d.strip()
        if d: self.text.append(d)

def fetch(url):
    req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8","ignore")

def rough_extract(html):
    # Try to find a recent result snippet. This is intentionally simple:
    # look for something that smells like a table row with place + date.
    # Fallback to "No recent result".
    t = TextGrab(); t.feed(html)
    s = " ".join(t.text)
    # crude patterns
    m = re.search(r"(Place|Rank)\s*[:\-]?\s*(\d{1,2})", s, re.I)
    place = m.group(2) if m else "—"
    m2 = re.search(r"(\d{4}-\d{2}-\d{2}|\d{1,2}\s\w+\s\d{4})", s)
    date = m2.group(1) if m2 else dt.date.today().isoformat()
    # location/event guesses
    m3 = re.search(r"(World Cup|Continental Cup|Nor-Am|FIS)\s*(.*?)\s*(Super\-G|Downhill|Moguls|Dual Moguls|HS\d+|Ski Jumping)", s, re.I)
    ev = (m3.group(3) if m3 else "Event")
    loc = "—"
    return place, date, ev, loc

def main():
    results=[]
    for name, default_event, url in ATHLETES:
        try:
            html = fetch(url)
            place, date, ev, loc = rough_extract(html)
            if ev=="Event": ev = default_event
            results.append({
              "athlete": name,
              "event": ev,
              "location": loc,
              "date": date,
              "place": place,
              "source": url
            })
        except Exception as e:
            results.append({
              "athlete": name,
              "event": default_event,
              "location": "—",
              "date": dt.date.today().isoformat(),
              "place": "—",
              "source": url
            })
    # Sort newest first (by date text best-effort)
    def key(r):
        try: return dt.datetime.fromisoformat(r["date"])
        except: return dt.datetime(1970,1,1)
    results.sort(key=key, reverse=True)
    os.makedirs("_data", exist_ok=True)
    with open("_data/results.yml","w") as f:
        yaml.safe_dump(results, f, sort_keys=False, allow_unicode=True)
    print("Wrote _data/results.yml with", len(results), "rows")
if __name__=="__main__":
    main()
