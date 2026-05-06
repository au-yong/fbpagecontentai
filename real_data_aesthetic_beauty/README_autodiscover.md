# Auto-Discover Malaysian Aesthetic / Skin Care / Beauty Companies

New script: `discover_real_companies.py`

This script can **automatically search online** for real companies without you providing any URLs.

Features:
- Searches DuckDuckGo for common keywords
- Finds new clinic websites automatically
- Scrapes Phone + WhatsApp
- Appends to your existing CSV + JSON backup
- Fully PDPA compliant (public data only)

## How to use

1. Activate virtual environment:
   ```bash
   cd /home/auyong/projects/fbpagecontentai/real_data_aesthetic_beauty
   source venv/bin/activate
   ```

2. Run auto-discovery:
   ```bash
   python discover_real_companies.py
   ```

The script will:
- Search 7 different targeted queries (KL, Penang, JB, Subang, etc.)
- Show you the new companies found
- Ask for confirmation before scraping contact details
- Save everything automatically

This is the "no manual search" solution you asked for.