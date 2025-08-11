# scripts/fetch_fis_results.py
from pathlib import Path
import json, urllib.parse as up
from playwright.sync_api import sync_playwright

ATHLETES = [
  {"name":"Sam Macuga","url":"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid=211435","discipline":"Ski Jumping"},
  {"name":"Lauren Macuga","url":"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=228398","discipline":"Alpine (DH, SG)"},
  {"name":"Alli Macuga","url":"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=FS&competitorid=220306","discipline":"Moguls"},
  {"name":"Daniel Macuga","url":"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=AL&competitorid=260517","discipline":"Alpine (all)"},
]

OUT = Path("assets/data/fis_results.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

def q(url, key):
    return up.parse_qs(up.urlparse(url).query).get(key, [""])[0]

def get_three_rows(page, url):
    # land directly on results tab; still click just in case
    page.goto(url + "#results", wait_until="domcontentloaded")

    # dismiss cookie banners occasionally blocking clicks
    for sel in [
        'button:has-text("Accept")',
        'button:has-text("I Accept")',
        'button:has-text("OK")',
        '[id*="accept"]',
    ]:
        try: page.locator(sel).first.click(timeout=1500)
        except: pass

    # ensure the Results tab is active / rendered
    try: page.get_by_role("tab", name="Results").click(timeout=2500)
    except: pass

    # wait for any table rows
    page.wait_for_selector("table tbody tr", timeout=12000)

    rows = page.locator("table tbody tr")
    out = []
    count = min(rows.count(), 3)
    for i in range(count):
        tds = rows.nth(i).locator("td")
        cols = [tds.nth(k).inner_text().strip() for k in range(tds.count())]

        # FIS table order (varies by sport). These are the common ones:
        # Date | Place | Nation | Category | Discipline | Position | FIS Points | Cup points
        def safe(idx): return cols[idx] if idx < len(cols) else ""

        date       = safe(0)
        place      = safe(1)
        category   = safe(3)
        discipline = safe(4)
        position   = safe(5)
        points     = safe(6)  # FIS points

        race = f"{category} — {discipline}".strip(" —")
        out.append({
            "date": date,
            "discipline": discipline or category,
            "race": race,
            "place": position,
            "points": points
        })
    return out

def main():
    data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126 Safari/537.36"
        ))
        page = ctx.new_page()

        for a in ATHLETES:
            try:
                results = get_three_rows(page, a["url"])
            except Exception as e:
                print(f"[warn] {a['name']}: {e}")
                results = []

            data[a["name"]] = {
                "fis_id": q(a["url"], "competitorid"),
                "sector": q(a["url"], "sectorcode"),
                "discipline": a["discipline"],
                "url": a["url"],
                "results": results
            }

        OUT.write_text(json.dumps(data, indent=2))
        print(f"wrote {OUT}")
        browser.close()

if __name__ == "__main__":
    main()
