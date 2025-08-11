# scripts/fetch_fis.py
import json, time, re, pathlib, urllib.parse
import requests
from bs4 import BeautifulSoup as BS
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"
DATA.mkdir(exist_ok=True)

athletes = yaml.safe_load((DATA / "athletes.yml").read_text())["athletes"]

UA = {"User-Agent": "TeamMacugaBot/1.0 (+github actions)"}

def parse_qs(url):
    q = urllib.parse.urlparse(url).query
    return {k:v[0] for k,v in urllib.parse.parse_qs(q).items()}

def fetch_results(sector, competitor_id, limit=15):
    # Results page
    url = ("https://www.fis-ski.com/DB/general/athlete-biography.html"
           f"?sectorcode={sector}&competitorid={competitor_id}&type=result")
    r = requests.get(url, headers=UA, timeout=20)
    r.raise_for_status()
    soup = BS(r.text, "lxml")

    # Heuristic: first table with tbody rows is usually the results table
    table = soup.select_one("table tbody")
    rows = []
    if table:
        for tr in table.select("tr")[:limit]:
            tds = [td.get_text(" ", strip=True) for td in tr.select("td")]
            if len(tds) < 4: 
                continue
            # FIS layouts vary by discipline; capture common bits
            # Typically: Date | Place | Category/Discipline | Race | City/Country | Points ...
            date = tds[0]
            place = re.sub(r"\D+$", "", tds[1])  # strip tied symbols etc
            desc  = tds[2] if len(tds) > 2 else ""
            race  = tds[3] if len(tds) > 3 else ""
            extra = " • ".join(tds[4:6]) if len(tds) > 5 else (tds[4] if len(tds) > 4 else "")
            pts   = tds[-1] if tds and tds[-1].replace(".","",1).isdigit() else ""

            rows.append({
                "date": date,
                "place": place,
                "discipline": desc,
                "race": race,
                "meta": extra,
                "points": pts,
                "source": url
            })
    return rows

out = {}
for a in athletes:
    qs = parse_qs(a["url"])
    sector = qs.get("sectorcode", "AL")
    cid    = qs.get("competitorid")
    if not cid:
        continue
    try:
        out[a["name"]] = {
            "fis_id": cid,
            "sector": sector,
            "discipline": a.get("discipline",""),
            "results": fetch_results(sector, cid, limit=15)
        }
        time.sleep(1.5)  # be polite
    except Exception as e:
        print("Error:", a["name"], e)

(DATA / "fis_results.json").write_text(json.dumps(out, indent=2))
print("Wrote _data/fis_results.json")
