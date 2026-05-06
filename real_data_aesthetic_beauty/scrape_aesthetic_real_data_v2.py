#!/usr/bin/env python3
"""
Real Malaysian Aesthetic / Aesthetic / Beauty Management Company Scraper v2
Features:
- Seeds
- Supports adding many new company URLs
- WhatsApp + Phone extraction
- JSON backup + CSV output
- PDPA compliant
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import re
import time
import argparse
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "real_aesthetic_beauty_companies.csv"
JSON_FILE = BASE_DIR / "real_aesthetic_beauty_collected.json"
USER_AGENT = "Mozilla/5.0 (compatible; Hermes-RealDataBot/2.0)"
PAUSE = 2.2

PDPA_TEXT = """This script only scrapes publicly listed business contact information.
Complies with PDPA for B2B research. Always verify data before outreach."""

def polite_get(url):
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        time.sleep(PAUSE)
        return resp if resp.status_code == 200 else None
    except Exception:
        return None

def extract_contacts(text, soup):
    phone_pattern = r'(?:\+?60|0)[\s-]?\d{1,3}[\s-]?\d{3,4}[\s-]?\d{3,4}'
    phones = re.findall(phone_pattern, text)
    phone = phones[0] if phones else ""

    whatsapp = ""
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if "wa.me" in href or "whatsapp" in href:
            whatsapp = a["href"]
            break
    if not whatsapp:
        wa = re.findall(r'(wa\.me/[\d+]+)', text, flags=re.IGNORECASE)
        if wa:
            whatsapp = wa[0]
    return phone, whatsapp

def scrape_single_company(url, name="Unknown"):
    resp = polite_get(url)
    if not resp:
        return None
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    phone, whatsapp = extract_contacts(text, soup)
    return {
        "company_name": name,
        "phone": phone,
        "whatsapp": whatsapp,
        "website": url,
        "source_notes": "Script-scraped",
        "date_collected": datetime.now().strftime("%Y-%m-%d")
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add-urls", nargs="+", help="List of new company websites to scrape")
    args = parser.parse_args()

    print(PDPA_TEXT)

    # Load existing data (CSV)
    fieldnames = ["No", "Company Name", "Category", "City/State", "Address", "Phone",
                  "WhatsApp", "Website", "Google Rating", "Source Notes", "Date Collected"]
    data = []
    if CSV_FILE.exists():
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

    next_no = len(data) + 1

    if args.add_urls:
        print(f"\n=== Adding {len(args.add_urls)} new companies ===")
        for url in args.add_urls:
            result = scrape_single_company(url)
            if result:
                result["No"] = next_no
                result["Category"] = "Aesthetic Clinic / Skin Care"
                result["City/State"] = ""
                result["Address"] = ""
                result["Google Rating"] = ""
                data.append(result)
                next_no += 1
                print(f"  + Added: {url}")
            else:
                print(f"  - Failed:  {url}")

    # Save updated CSV
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    # Save JSON backup
    backup = {
        "metadata": {
            "total_real_companies": len(data),
            "last_updated": datetime.now().isoformat(),
            "disclaimer": PDPA_TEXT
        },
        "companies": data
    }
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(backup, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Total real companies now: {len(data)}")
    print(f"CSV saved:  {CSV_FILE}")
    print(f"JSON saved: {JSON_FILE}")

if __name__ == "__main__":
    main()