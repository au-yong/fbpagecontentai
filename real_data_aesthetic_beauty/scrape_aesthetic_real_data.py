#!/usr/bin/env python3
"""
Real Malaysian Aesthetic / Skin Care / Beauty Scraper
Version: v1.0 (Ethical Public Sources Only)

Features:
- Scrapes public websites for contact info (Phone + WhatsApp)
- Updates the master CSV + JSON backup
- Rate limited + polite headers
- PDPA compliant disclaimer in every run

WARNING:
This script ONLY touches PUBLICLY available information.
Never scrape private data, never use for spam.
User must verify all scraped data before outreach.

Usage examples:
    python scrape_aesthetic_real_data.py --mode enhance-seed
    python scrape_aesthetic_real_data.py --mode add-new --url https://exampleclinic.com.my

Requirements:
pip install requests beautifulsoup4 pandas
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

# ====================== CONFIG ======================
BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "real_aesthetic_beauty_companies.csv"
JSON_FILE = BASE_DIR / "real_aesthetic_beauty_collected.json"
USER_AGENT = "Mozilla/5.0 (compatible; Hermes-RealDataBot/1.0; +https://github.com/au-yong)"
PAUSE = 2.5  # seconds between requests (be polite)

# PDPA Disclaimer
PDPA_TEXT = """This script collects only publicly listed business contact information.
All data is used strictly for B2B research under PDPA guidelines.
Verify contact details yourself before any outreach."""

# ====================== HELPERS ======================
def polite_get(url):
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html"}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        time.sleep(PAUSE)
        return resp
    except Exception as e:
        print(f"[ERROR] Could not fetch {url}: {e}")
        return None

def extract_phone(text):
    """Extract Malaysian phone numbers"""
    pattern = r'(?:\+?60|0)[\s-]?\d{1,3}[\s-]?\d{3,4}[\s-]?\d{3,4}'
    matches = re.findall(pattern, text)
    return matches[0] if matches else ""

def extract_whatsapp(text):
    """Look for WhatsApp or wa.me links"""
    wa_pattern = r'(?:wa\.me/|whatsapp.*?\+?60|wa\.me/\d+)[\d\s-]{8,15}'
    matches = re.findall(wa_pattern, text, re.I)
    return matches[0] if matches else ""

def scrape_website(url):
    """Scrape a single public clinic website for contact info"""
    resp = polite_get(url)
    if not resp or resp.status_code != 200:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    full_text = soup.get_text(" ", strip=True)

    phone = extract_phone(full_text)
    whatsapp = extract_whatsapp(full_text)

    # Try finding WhatsApp specifically in links
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if "wa.me" in href or "whatsapp" in href:
            whatsapp = a["href"]
            break

    return {
        "phone": phone,
        "whatsapp": whatsapp,
        "source_url": url,
        "last_scraped": datetime.now().isoformat()
    }

# ====================== CORE FUNCTIONS ======================
def enhance_seed_data():
    """Load the seed CSV and try to enrich with contact info"""
    print("[INFO] Enhancing seed real data with public website scraping...")
    existing = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        existing = list(reader)

    enhanced = []
    for row in existing:
        url = row.get("Website", "").strip()
        if url and url.startswith("http"):
            print(f"  → Scraping: {row['Company Name'][:40]}")
            scraped = scrape_website(url)
            if scraped:
                row["Phone"] = scraped["phone"] or row["Phone"]
                row["WhatsApp"] = scraped["whatsapp"] or row["WhatsApp"]
        enhanced.append(row)

    # Save updated CSV
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(enhanced)

    # Backup to JSON
    backup_to_json(enhanced)
    print(f"\n[OK] Enhanced {len(enhanced)} real companies.")
    print(f"     CSV updated: {CSV_FILE}")
    print(f"     Backup JSON: {JSON_FILE}")

def backup_to_json(companies_list):
    """Create a full JSON backup with metadata"""
    data = {
        "metadata": {
            "total_real_companies": len(companies_list),
            "last_updated": datetime.now().isoformat(),
            "source": "Public websites + manual seed",
            "disclaimer": PDPA_TEXT,
            "script_version": "1.0"
        },
        "companies": companies_list
    }
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[INFO] JSON backup saved ({len(companies_list)} companies)")

def main():
    parser = argparse.ArgumentParser(description="Real Malaysian Aesthetic Data Scraper")
    parser.add_argument("--mode", choices=["enhance-seed"], default="enhance-seed",
                        help="enhance-seed = scrape the existing 30 real companies")
    args = parser.parse_args()

    print("=== Real Aesthetic / Skin Care Scraper ===")
    print(PDPA_TEXT)
    print()

    if args.mode == "enhance-seed":
        enhance_seed_data()
    else:
        print("Mode not implemented yet.")

if __name__ == "__main__":
    main()