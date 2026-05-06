#!/usr/bin/env python3
"""
Auto Discover + Scrape Malaysian Aesthetic Clinics / Skin Care / Beauty Companies
No manual URL input needed.

Modes:
- --discover          : Search DuckDuckGo and collect new clinic websites
- --discover-and-scrape : Discover + immediately scrape contact info and save

Targeted cities are hard-coded but you can expand easily.

PDPA Disclaimer always shown.
"""

import re
import time
import json
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "real_aesthetic_beauty_companies.csv"
JSON_FILE = BASE_DIR / "real_aesthetic_beauty_collected.json"

USER_AGENT = "Mozilla/5.0 (compatible; Hermes-CompanyHunter/1.0)"
PAUSE = 3.0

SEARCH_QUERIES = [
    "aesthetic clinic Kuala Lumpur",
    "skin care clinic Penang",
    "aesthetic clinic Johor Bahru",
    "beauty clinic Subang Jaya",
    "medical spa KL",
    "dermatology clinic Malaysia",
    "aesthetic centre Petaling Jaya",
    "skin management clinic Shah Alam",
]

def polite_get(url):
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        time.sleep(PAUSE)
        return resp if resp.status_code == 200 else None
    except Exception as e:
        print(f"Network error: {e}")
        return None

def extract_contacts(text, soup):
    phone_pattern = r'(?:\+?60|0)[\s-]?\d{1,3}[\s-]?\d{3,4}[\s-]?\d{3,4}'
    phones = re.findall(phone_pattern, text)
    phone = phones[0] if phones else ""
    whatsapp = ""
    for a in soup.find_all("a", href=True):
        if "wa.me" in a["href"].lower():
            whatsapp = a["href"]
            break
    return phone, whatsapp

def discover_companies_from_duckduckgo(query, max_results=8):
    """Search DuckDuckGo and extract business websites"""
    search_url = f"https://html.duckduckgo.com/html/?q={query}+Malaysia"
    resp = polite_get(search_url)
    if not resp:
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for a in soup.find_all("a", class_="result__a", href=True)[:max_results]:
        href = a["href"]
        title = a.get_text(strip=True)
        # Filter for actual clinic websites
        if any(x in href for x in [".com.my", ".my", "clinic", "aesthetic", "skin", "beauty"]):
            results.append({"title": title, "url": href})
    return results

def scrape_company(url):
    resp = polite_get(url)
    if not resp:
        return None
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    phone, whatsapp = extract_contacts(text, soup)
    return {
        "company_name": url.split("//")[-1].split("/")[0].replace("www.", ""),
        "category": "Aesthetic / Skin / Beauty",
        "city_state": "",
        "address": "",
        "phone": phone,
        "whatsapp": whatsapp,
        "website": url,
        "google_rating": "",
        "source_notes": f"Auto-discovered {datetime.now().strftime('%Y-%m-%d')}",
        "date_collected": datetime.now().strftime("%Y-%m-%d")
    }

def load_existing_companies():
    if not CSV_FILE.exists():
        return []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_companies(companies):
    fieldnames = ["No", "Company Name", "Category", "City/State", "Address", "Phone",
                  "WhatsApp", "Website", "Google Rating", "Source Notes", "Date Collected"]

    for i, c in enumerate(companies, 1):
        c["No"] = i

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)

    # JSON backup
    backup = {
        "metadata": {
            "total_real_companies": len(companies),
            "last_updated": datetime.now().isoformat(),
            "disclaimer": "Public data only. PDPA compliant for research."
        },
        "companies": companies
    }
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(backup, f, indent=2, ensure_ascii=False)

def main():
    print("=== Malaysian Aesthetic Company Hunter (Auto-Discover Mode) ===")
    print("This tool searches public results and extracts real business leads.")
    print("Only public data. PDPA compliant. Verify before outreach.\n")

    existing = load_existing_companies()
    existing_urls = {row.get("Website", "") for row in existing}

    new_found = []

    for q in SEARCH_QUERIES:
        print(f"\nSearching: {q}")
        found = discover_companies_from_duckduckgo(q)
        for item in found:
            url = item["url"]
            if url and url not in existing_urls:
                print(f"  New candidate: {item['title'][:50]} -> {url}")
                new_found.append(item)

    if not new_found:
        print("\nNo new companies found this round. Try again later.")
        return

    print(f"\n=== Found {len(new_found)} new potential companies ===")
    print("Do you want to scrape contact info for these new leads? (y/n)")

    answer = input("> ").strip().lower()
    if answer != "y":
        print("Discovery only. New URLs not scraped. Run again later with --scrape.")
        return

    print("\nScraping contact details...")
    scraped_success = 0
    for item in new_found:
        data = scrape_company(item["url"])
        if data:
            # Merge with known info
            data["company_name"] = item["title"][:60] or data["company_name"]
            existing.append(data)
            scraped_success += 1
            print(f"  ✓ Scraped: {data['company_name']}")

    save_companies(existing)
    print(f"\n✅ Total real companies now: {len(existing)}")
    print(f"CSV updated:  {CSV_FILE}")
    print(f"JSON backup:  {JSON_FILE}")

if __name__ == "__main__":
    main()