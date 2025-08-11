# scripts/fis_fetch_xhr.py
import json, re, time, pathlib, yaml
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
ATH = yaml.safe_load((ROOT / "_data" / "athletes.yml").read_text())["athletes"]

def parse_three_rows_from_dom(page):
    # DOM fallback if XHR matching fails
    page.wait_for_timeout(1500)
    rows = page.query_selector_all("table tbody tr")[:3]
    out = []
    for tr in rows:
        tds = [c.inner_text().strip() for c in tr.query_selector_all("td")]
        if not tds:
            continue
        # FIS columns are usually:
        # Date | Place | Nation | Category | Discipline | Position | FIS Points | Cup points
        m = {
            "date": tds[0] if len(tds) > 0 else "",
            "discipline": tds[4] if len(tds) > 4 else "",
            "race": f"{tds[1]} — {tds[3]}"[:120] if len(tds) > 3 else "",
            "place": tds[5] if len(tds) > 5 else "",
            "points": tds[6] if len(tds) > 6 else "",
            "source": page.url
        }
        out.append(m)
    return out

def fetch_one(pw, name, url, discipline):
    browser = pw.chromium.launch(headless=True)
    ctx = browser.new_context()
    page = ctx.new_page()

    # collect XHR that looks like the results feed
    captured = []
    def grab(resp):
        u = resp.url
        if "data" in u or "result" in u.lower():
            if resp.request.resource_type == "xhr":
                captured.append(resp)
    page.on("response", grab)

    page.goto(url, timeout=60000, wait_until="domcontentloaded")

    # cookie banners sometimes block clicks
    for sel in ('button:has-text("Accept")', 'button:has-text("I agree")'):
        try:
            page.locator(sel).first.click(timeout=1500)
        except Exception:
            pass

    # go to Results tab (try several selectors)
    for sel in ('[role="tab"]:has-text("Results")',
                'a:has-text("Results")',
                'button:has-text("Results")'):
        try:
            page.locator(sel).first.click(timeout=4000)
            break
        except Exception:
            continue

    # give the XHR a moment
    page.wait_for_timeout(2500)

    results = []
    # prefer XHR JSON if we got one
    for resp in captured[::-1]:
        try:
            data = resp.json()
        except Exception:
            continue

        # map the first 3 entries — structure differs by discipline, so be defensive
        rows = data if isinstance(data, list) else data.get("results") or data.get("data") or []
        for r in rows[:3]:
            results.append({
                "date": r.get("date") or r.get("Date") or "",
                "discipline": r.get("discipline") or r.get("Discipline") or "",
                "race": r.get("event") or r.get("Race") or r.get("Category") or "",
                "place": r.get("rank") or r.get("Position") or r.get("Place") or "",
                "points": r.get("fisPoints") or r.get("FIS Points") or r.get("Pts") or "",
                "source": url
            })
        if results:
            break

    # fallback to parsing the DOM if no usable XHR
    if not results:
        results = parse_three_rows_from_dom(page)

    browser.close()
    return results

def main():
    out = {}
    with sync_playwright() as pw:
        for a in ATH:
            m = re.search(r"competitorid=(\d+).*sectorcode=([A-Z]+)", a["url"])
            fis_id = m.group(1) if m else ""
            sector = m.group(2) if m else ""
            print(f"Fetching: {a['name']} …")
            try:
                rows = fetch_one(pw, a["name"], a["url"], a.get("discipline",""))
            except Exception as e:
                print(f"[warn] {a['name']}: {e}")
                rows = []
            out[a["name"]] = {
                "fis_id": fis_id,
                "sector": sector,
                "discipline": a.get("discipline",""),
                "results": rows
            }

    (ROOT / "_data" / "fis_results.json").write_text(json.dumps(out, indent=2))
    print("Wrote _data/fis_results.json")

if __name__ == "__main__":
    main()
