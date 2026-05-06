#!/usr/bin/env python3
"""
Hard scraper for LPEPH BIS portal
Attempts to find API endpoints and extract property firm/negotiator data
"""
import requests
import json
import re
from bs4 import BeautifulSoup

def inspect_page_source(url):
    """Inspect page source for API endpoints"""
    print(f"\n=== Inspecting {url} ===")
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })
    
    try:
        resp = session.get(url, timeout=10)
        html = resp.text
        
        # Look for API endpoints in JavaScript
        api_patterns = [
            r'https?://[^"\'\s]+(?:api|search|ajax|endpoint)[^"\'\s]*',
            r'/(?:api|search|ajax|endpoint)/[^"\'\s]*',
            r'url\s*:\s*["\'](/[^"\']+)["\']',
            r'action\s*=\s*["\']([^"\']+)["\']',
        ]
        
        print(f"Status: {resp.status_code}")
        print(f"Found API patterns:")
        
        for i, pattern in enumerate(api_patterns):
            matches = re.findall(pattern, html)
            if matches:
                print(f"  Pattern {i}: {list(set(matches))[:5]}")
        
        # Look for form actions
        soup = BeautifulSoup(html, 'html.parser')
        forms = soup.find_all('form')
        print(f"\nForms found: {len(forms)}")
        for i, form in enumerate(forms):
            print(f"  Form {i}: action='{form.get('action')}' method='{form.get('method')}'")
        
        # Look for iframe sources
        iframes = soup.find_all('iframe')
        print(f"\nIframes found: {len(iframes)}")
        for i, iframe in enumerate(iframes):
            print(f"  Iframe {i}: src='{iframe.get('src')}'")
            
        # Check for any AJAX configurations
        scripts = soup.find_all('script')
        print(f"\nScripts found: {len(scripts)}")
        for i, script in enumerate(scripts):
            if script.string and ('fetch(' in script.string or 'ajax(' in script.string or 'axios' in script.string):
                print(f"  Script {i} has AJAX calls")
                # Extract URLs from script
                urls = re.findall(r'["\'](https?://[^"\']+)["\']', script.string)
                if urls:
                    print(f"    URLs: {urls[:3]}")
        
        return session, html
        
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def try_api_endpoints(session):
    """Try common API endpoints"""
    print("\n=== Trying API Endpoints ===")
    
    base_url = "https://bis.lpeph.gov.my"
    endpoints = [
        "/api/search/firm",
        "/api/firm/search",
        "/search/api",
        "/api/v1/search",
        "/rest/firm/list",
        "/api/negotiator/search",
        "/api/member/search",
    ]
    
    for endpoint in endpoints:
        url = base_url + endpoint
        print(f"\nTrying: {url}")
        try:
            resp = session.get(url, timeout=5)
            print(f"  Status: {resp.status_code}")
            if resp.status_code == 200:
                print(f"  Response: {resp.text[:200]}")
        except Exception as e:
            print(f"  Error: {e}")

def main():
    # Inspect main page
    session, html = inspect_page_source("https://bis.lpeph.gov.my/search")
    
    if session:
        # Try API endpoints
        try_api_endpoints(session)
        
        # Try to submit search form
        print("\n=== Attempting Form Submission ===")
        try:
            resp = session.post("https://bis.lpeph.gov.my/search", 
                              data={'firmName': 'a', 'search': 'Search'},
                              headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(f"POST Status: {resp.status_code}")
            print(f"Response preview: {resp.text[:500]}")
        except Exception as e:
            print(f"POST Error: {e}")
    
    print("\n=== Done ===")

if __name__ == "__main__":
    main()
