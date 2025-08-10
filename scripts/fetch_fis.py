import re, sys, time, json, yaml, pathlib
from datetime import datetime
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "_data" / "fis_sources.yml"
OUT = ROOT / "_data" / "results_auto.yml"

def load_sources():
    with open(SRC, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["athletes"]

def fetch(url):
    # Be polite
    headers = {
        "User-Agent": "TeamMacugaBot/1.0 (+github actions) requests"
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.text

def parse_latest(html):
    """
    Tries to find the latest result row on an athlete page.
    FIS pages are server-rendered; look for the first row in a results table.
    Return dict with date, event, place/result (e.g., '1st'), discipline if found.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Common pattern: the first table row in a 'g-table' or 'table' with results
    tables = []
    for sel in ["table.g-table", "table", "div.g-table"]:
        tables += soup.select(sel)

    for tbl in tables:
        # find rows with cells
        rows = tbl.select("tbody tr") or tbl.select("tr")
        for tr in rows:
            tds = [td.get_text(" ", strip=True) for td in tr.find_all(["td","th"])]
            if len(tds) < 3: 
                continue

            # Heuristics: a date in first 2 cells
            date_str = None
            for c in tds[:3]:
                m = re.search(r"\b(\d{1,2}\.\d{1,2}\.\d{2,4})\b", c)  # e.g., 12.01.2025
                if m:
                    date_str = m.group(1)
                    break

            # Event / place heuristics
            txt = " | ".join(tds)
            # Place like 1, 2, 3, 10 etc. sometimes with symbols; normalize to 1st/2nd/3rd/th
            place = None
            pm = re.search(r"\b(\d{1,2})\b", txt)
            if pm:
                n = int(pm.group(1))
                suffix = "th"
                if n % 10 == 1 and n % 100 != 11: suffix = "st"
                elif n % 10 == 2 and n % 100 != 12: suffix = "nd"
                elif n % 10 == 3 and n % 100 != 13: suffix = "rd"
                place = f"{n}{suffix}"

            # Event name guess
            # Look for something with 'World Cup'/'Continental Cup'/'Nationals' etc.
            em = re.search(r"(World Cup|Continental Cup|Worlds|National|NC|COC|FIS Cup|NorAm|Europa Cup)", txt, re.I)
            event = em.group(1) if em else None

            # If we have at least date and place, call it a row
            if date_str and place:
                try:
                    d = datetime.strptime(date_str, "%d.%m.%Y").date().isoformat()
                except ValueError:
                    try:
                        d = datetime.strptime(date_str, "%d.%m.%y").date().isoformat()
                    except Exception:
                        d = date_str
                return {"date": d, "event": event or "Latest competition", "result": place}
    return None

def main():
    sources = load_sources()
    results = []
    for a in sources:
        try:
            html = fetch(a["url"])
            latest = parse_latest(html)
            if latest:
                results.append({
                    "date": latest["date"],
                    "athlete": a["name"],
                    "discipline": a.get("discipline",""),
                    "event": latest["event"],
                    "result": latest["result"],
                    "link": a["url"]
                })
            time.sleep(1.5)  # be gentle
        except Exception as e:
            # record a note instead of failing all
            results.append({
                "date": datetime.utcnow().date().isoformat(),
                "athlete": a["name"],
                "discipline": a.get("discipline",""),
                "event": "Could not fetch",
                "result": "—",
                "link": a["url"]
            })

    # Sort newest first
    results.sort(key=lambda r: r["date"], reverse=True)
    with open(OUT, "w", encoding="utf-8") as f:
        yaml.safe_dump(results, f, sort_keys=False, allow_unicode=True)

if __name__ == "__main__":
    main()
