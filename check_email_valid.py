#!/usr/bin/env python3
"""
Email Validation Script for lpeph_negotiators_20260505_010015.json
=================================================================
Checks all email addresses in the negotiator data to ensure they are
valid and safe to send before running an email campaign.

Validation checks:
  1. Empty/missing emails
  2. Email format (RFC 5322 regex)
  3. Disposable/temporary email domains
  4. Common typos in popular domains
  5. Duplicate emails
  6. MX record verification (DNS check)
  7. Role-based emails (info@, admin@, etc.)
  8. Suspicious patterns (test, example, etc.)

Usage:
  python check_email_valid.py
  python check_email_valid.py --dns          # Include MX record checks (slower)
  python check_email_valid.py --export       # Export clean list to CSV
  python check_email_valid.py --dns --export # Both DNS checks and CSV export
"""

import json
import re
import sys
import os
import csv
import argparse
from collections import Counter, defaultdict
from datetime import datetime

# Fix Windows console encoding for emoji/unicode output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")

# ─── Configuration ───────────────────────────────────────────────────────────

INPUT_FILE = "lpeph_negotiators_20260505_010015.json"
OUTPUT_CSV = "negotiators_clean_emails.csv"
OUTPUT_REPORT = "email_validation_report.txt"

# RFC 5322-ish email regex (covers 99%+ of real-world valid emails)
EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"
)

# Common disposable/temporary email domains
DISPOSABLE_DOMAINS = {
    "mailinator.com", "guerrillamail.com", "tempmail.com", "throwaway.email",
    "yopmail.com", "sharklasers.com", "guerrillamailblock.com", "grr.la",
    "dispostable.com", "trashmail.com", "fakeinbox.com", "mailnesia.com",
    "maildrop.cc", "discard.email", "temp-mail.org", "getnada.com",
    "mohmal.com", "burnermail.io", "tempail.com", "10minutemail.com",
    "minutemail.com", "emailondeck.com", "tempr.email", "temp-mail.io",
}

# Role-based email prefixes (generally lower engagement, higher bounce)
ROLE_BASED_PREFIXES = {
    "info", "admin", "support", "sales", "contact", "help", "service",
    "billing", "webmaster", "postmaster", "hostmaster", "abuse",
    "noreply", "no-reply", "mailer-daemon", "marketing", "office",
    "enquiry", "enquiries", "feedback", "general", "hr", "jobs",
    "careers", "reception", "accounts",
}

# Common domain typos -> suggested correction
DOMAIN_TYPOS = {
    "gmial.com": "gmail.com",
    "gmal.com": "gmail.com",
    "gmaill.com": "gmail.com",
    "gamil.com": "gmail.com",
    "gnail.com": "gmail.com",
    "gmsil.com": "gmail.com",
    "gmali.com": "gmail.com",
    "gmail.co": "gmail.com",
    "gmail.con": "gmail.com",
    "gmail.cm": "gmail.com",
    "gmail.om": "gmail.com",
    "gmail.cim": "gmail.com",
    "gmail.vom": "gmail.com",
    "gmail.comm": "gmail.com",
    "gmai.com": "gmail.com",
    "gmailcom": "gmail.com",
    "g.mail.com": "gmail.com",
    "htomail.com": "hotmail.com",
    "hotmial.com": "hotmail.com",
    "hotmal.com": "hotmail.com",
    "hotmai.com": "hotmail.com",
    "hotmail.co": "hotmail.com",
    "hotmail.con": "hotmail.com",
    "hotmaill.com": "hotmail.com",
    "hotamil.com": "hotmail.com",
    "htmail.com": "hotmail.com",
    "yahooo.com": "yahoo.com",
    "yaho.com": "yahoo.com",
    "yahoo.co": "yahoo.com",
    "yahoo.con": "yahoo.com",
    "yhoo.com": "yahoo.com",
    "yhaoo.com": "yahoo.com",
    "outllook.com": "outlook.com",
    "outlok.com": "outlook.com",
    "outook.com": "outlook.com",
    "outlook.co": "outlook.com",
}

# Suspicious patterns in local part
SUSPICIOUS_PATTERNS = [
    re.compile(r"^test[0-9]*@", re.I),
    re.compile(r"^example@", re.I),
    re.compile(r"^user[0-9]*@", re.I),
    re.compile(r"^fake@", re.I),
    re.compile(r"^none@", re.I),
    re.compile(r"^null@", re.I),
    re.compile(r"^asdf@", re.I),
    re.compile(r"^abc@", re.I),
    re.compile(r"^xxx@", re.I),
    re.compile(r"^aaa@", re.I),
    re.compile(r"^sample@", re.I),
    re.compile(r"^demo@", re.I),
    re.compile(r"@example\.", re.I),
    re.compile(r"@test\.", re.I),
    re.compile(r"@localhost", re.I),
]


# ─── Helpers ─────────────────────────────────────────────────────────────────

class Colors:
    """ANSI color codes for terminal output."""
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def c(text, color):
    return f"{color}{text}{Colors.RESET}"


def bar_chart(label, count, total, width=40, color=Colors.GREEN):
    """Render a simple horizontal bar chart line."""
    pct = (count / total * 100) if total else 0
    filled = int(width * count / total) if total else 0
    bar = "█" * filled + "░" * (width - filled)
    return f"  {label:<28} {color}{bar}{Colors.RESET} {count:>6} ({pct:5.1f}%)"


# ─── Validation Functions ───────────────────────────────────────────────────

def validate_format(email):
    """Check if email matches valid format."""
    return bool(EMAIL_REGEX.match(email))


def check_disposable(domain):
    """Check if domain is a known disposable email provider."""
    return domain.lower() in DISPOSABLE_DOMAINS


def check_typo(domain):
    """Check if domain looks like a typo of a common provider."""
    return DOMAIN_TYPOS.get(domain.lower())


def check_role_based(local_part):
    """Check if email is a role-based address."""
    return local_part.lower() in ROLE_BASED_PREFIXES


def check_suspicious(email):
    """Check if email matches suspicious patterns."""
    for pattern in SUSPICIOUS_PATTERNS:
        if pattern.search(email):
            return True
    return False


def check_mx_record(domain):
    """Check if domain has valid MX records (requires dnspython)."""
    try:
        import dns.resolver
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            return len(answers) > 0
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN,
                dns.resolver.NoNameservers, dns.exception.Timeout):
            return False
    except ImportError:
        return None  # dnspython not installed


# ─── Main Validation Pipeline ───────────────────────────────────────────────

def validate_emails(data, do_dns=False):
    """
    Run all validation checks on the dataset.
    Returns categorized results.
    """
    results = {
        "total": len(data),
        "empty_email": [],
        "invalid_format": [],
        "disposable": [],
        "typo_domain": [],
        "role_based": [],
        "suspicious": [],
        "duplicate": [],
        "no_mx": [],
        "valid": [],
        "domain_stats": Counter(),
        "all_issues": defaultdict(list),  # email -> list of issues
    }

    email_seen = Counter()

    # First pass: collect all emails for duplicate detection
    for rec in data:
        email = (rec.get("email") or "").strip()
        if email:
            email_seen[email.lower()] += 1

    # Second pass: validate each record
    checked_mx = {}  # cache MX lookups
    for i, rec in enumerate(data):
        email = (rec.get("email") or "").strip()
        name = (rec.get("full_name") or "").strip()
        ren = rec.get("ren_no") or "N/A"
        entry = {"index": i, "email": email, "name": name, "ren_no": ren, "record": rec}
        issues = []

        # 1. Empty email
        if not email:
            results["empty_email"].append(entry)
            continue

        # 2. Format check
        if not validate_format(email):
            results["invalid_format"].append(entry)
            issues.append("invalid_format")

        # Parse parts
        parts = email.rsplit("@", 1)
        if len(parts) == 2:
            local_part, domain = parts
        else:
            local_part, domain = email, ""

        # 3. Domain stats
        if domain:
            results["domain_stats"][domain.lower()] += 1

        # 4. Disposable domain
        if domain and check_disposable(domain):
            results["disposable"].append(entry)
            issues.append("disposable_domain")

        # 5. Typo check
        if domain:
            suggested = check_typo(domain)
            if suggested:
                entry["suggested_domain"] = suggested
                results["typo_domain"].append(entry)
                issues.append(f"typo_domain (did you mean @{suggested}?)")

        # 6. Role-based
        if local_part and check_role_based(local_part):
            results["role_based"].append(entry)
            issues.append("role_based")

        # 7. Suspicious
        if check_suspicious(email):
            results["suspicious"].append(entry)
            issues.append("suspicious_pattern")

        # 8. Duplicate
        if email_seen[email.lower()] > 1:
            results["duplicate"].append(entry)
            issues.append(f"duplicate ({email_seen[email.lower()]}x)")

        # 9. MX record check (optional, slow)
        if do_dns and domain and not issues:
            domain_lower = domain.lower()
            if domain_lower not in checked_mx:
                checked_mx[domain_lower] = check_mx_record(domain_lower)
            mx_ok = checked_mx[domain_lower]
            if mx_ok is False:
                results["no_mx"].append(entry)
                issues.append("no_mx_record")
            elif mx_ok is None and not hasattr(validate_emails, "_dns_warned"):
                print(c("  ⚠  dnspython not installed. Skipping MX checks.", Colors.YELLOW))
                print(c("     Install with: pip install dnspython", Colors.DIM))
                validate_emails._dns_warned = True

        # Categorize
        if issues:
            results["all_issues"][email] = issues
        else:
            results["valid"].append(entry)

        # Progress indicator
        if (i + 1) % 10000 == 0:
            print(f"\r  Processed {i+1:,}/{len(data):,} records...", end="", flush=True)

    if len(data) > 10000:
        print(f"\r  Processed {len(data):,}/{len(data):,} records...done!")

    return results


def print_report(results, do_dns=False):
    """Print a beautiful terminal report."""
    total = results["total"]
    n_empty = len(results["empty_email"])
    n_invalid = len(results["invalid_format"])
    n_disposable = len(results["disposable"])
    n_typo = len(results["typo_domain"])
    n_role = len(results["role_based"])
    n_suspicious = len(results["suspicious"])
    n_dup = len(results["duplicate"])
    n_no_mx = len(results["no_mx"])
    n_valid = len(results["valid"])
    n_has_email = total - n_empty
    n_problematic = n_invalid + n_disposable + n_typo + n_suspicious + n_no_mx

    print()
    print(c("=" * 72, Colors.CYAN))
    print(c("  📧  EMAIL VALIDATION REPORT", Colors.BOLD))
    print(c(f"  File: {INPUT_FILE}", Colors.DIM))
    print(c(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.DIM))
    print(c("=" * 72, Colors.CYAN))

    # ─── Overview ────────────────────────────────────────────────────────
    print(c("\n  📊 OVERVIEW", Colors.BOLD))
    print(f"  {'Total records:':<28} {c(f'{total:,}', Colors.BOLD)}")
    print(f"  {'With email:':<28} {c(f'{n_has_email:,}', Colors.GREEN)}")
    print(f"  {'Without email (empty):':<28} {c(f'{n_empty:,}', Colors.YELLOW)}")
    print(f"  {'Valid & sendable:':<28} {c(f'{n_valid:,}', Colors.GREEN)}")
    print(f"  {'With issues:':<28} {c(f'{n_problematic:,}', Colors.RED)}")

    # ─── Distribution Bar Chart ──────────────────────────────────────────
    print(c("\n  📈 DISTRIBUTION", Colors.BOLD))
    print(bar_chart("✅ Valid emails", n_valid, total, color=Colors.GREEN))
    print(bar_chart("📭 Empty (no email)", n_empty, total, color=Colors.YELLOW))
    print(bar_chart("❌ Invalid format", n_invalid, total, color=Colors.RED))
    print(bar_chart("🗑️  Disposable domain", n_disposable, total, color=Colors.RED))
    print(bar_chart("✏️  Typo in domain", n_typo, total, color=Colors.YELLOW))
    print(bar_chart("🏢 Role-based", n_role, total, color=Colors.YELLOW))
    print(bar_chart("🔍 Suspicious", n_suspicious, total, color=Colors.RED))
    print(bar_chart("👥 Duplicate emails", n_dup, total, color=Colors.YELLOW))
    if do_dns:
        print(bar_chart("🌐 No MX record", n_no_mx, total, color=Colors.RED))

    # ─── Invalid Format Examples ─────────────────────────────────────────
    if results["invalid_format"]:
        print(c(f"\n  ❌ INVALID FORMAT EMAILS ({n_invalid})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["invalid_format"][:20]:
            print(f"    {c(entry['email'], Colors.RED):<45} {Colors.DIM}{entry['name']}{Colors.RESET}")
        if n_invalid > 20:
            print(c(f"    ... and {n_invalid - 20} more", Colors.DIM))

    # ─── Typo Domain Examples ────────────────────────────────────────────
    if results["typo_domain"]:
        print(c(f"\n  ✏️  POSSIBLE TYPOS IN DOMAIN ({n_typo})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["typo_domain"][:20]:
            suggested = entry.get("suggested_domain", "?")
            print(f"    {c(entry['email'], Colors.YELLOW):<45} → {c(f'@{suggested}', Colors.GREEN)}")
        if n_typo > 20:
            print(c(f"    ... and {n_typo - 20} more", Colors.DIM))

    # ─── Suspicious Examples ─────────────────────────────────────────────
    if results["suspicious"]:
        print(c(f"\n  🔍 SUSPICIOUS EMAILS ({n_suspicious})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["suspicious"][:15]:
            print(f"    {c(entry['email'], Colors.RED):<45} {Colors.DIM}{entry['name']}{Colors.RESET}")
        if n_suspicious > 15:
            print(c(f"    ... and {n_suspicious - 15} more", Colors.DIM))

    # ─── Duplicate Emails ────────────────────────────────────────────────
    if results["duplicate"]:
        # Group duplicates
        dup_groups = defaultdict(list)
        for entry in results["duplicate"]:
            dup_groups[entry["email"].lower()].append(entry)
        
        n_dup_unique = len(dup_groups)
        print(c(f"\n  👥 DUPLICATE EMAILS ({n_dup} records, {n_dup_unique} unique emails)", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        shown = 0
        for email, entries in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
            if shown >= 10:
                break
            print(f"    {c(email, Colors.YELLOW)} × {len(entries)}")
            for e in entries[:3]:
                print(f"      └─ {Colors.DIM}{e['name']} ({e['ren_no']}){Colors.RESET}")
            if len(entries) > 3:
                print(f"      └─ {Colors.DIM}... and {len(entries) - 3} more{Colors.RESET}")
            shown += 1
        if n_dup_unique > 10:
            print(c(f"    ... and {n_dup_unique - 10} more duplicate groups", Colors.DIM))

    # ─── Disposable Domains ──────────────────────────────────────────────
    if results["disposable"]:
        print(c(f"\n  🗑️  DISPOSABLE EMAIL DOMAINS ({n_disposable})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["disposable"][:10]:
            print(f"    {c(entry['email'], Colors.RED):<45} {Colors.DIM}{entry['name']}{Colors.RESET}")

    # ─── Role-based Emails ───────────────────────────────────────────────
    if results["role_based"]:
        print(c(f"\n  🏢 ROLE-BASED EMAILS ({n_role})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["role_based"][:10]:
            print(f"    {c(entry['email'], Colors.YELLOW):<45} {Colors.DIM}{entry['name']}{Colors.RESET}")
        if n_role > 10:
            print(c(f"    ... and {n_role - 10} more", Colors.DIM))

    # ─── No MX Records ──────────────────────────────────────────────────
    if results["no_mx"]:
        print(c(f"\n  🌐 NO MX RECORD ({n_no_mx})", Colors.BOLD))
        print(c("  " + "─" * 68, Colors.DIM))
        for entry in results["no_mx"][:10]:
            print(f"    {c(entry['email'], Colors.RED):<45} {Colors.DIM}{entry['name']}{Colors.RESET}")
        if n_no_mx > 10:
            print(c(f"    ... and {n_no_mx - 10} more", Colors.DIM))

    # ─── Top Email Domains ───────────────────────────────────────────────
    print(c("\n  🌍 TOP 15 EMAIL DOMAINS", Colors.BOLD))
    print(c("  " + "─" * 68, Colors.DIM))
    for domain, count in results["domain_stats"].most_common(15):
        pct = count / n_has_email * 100
        print(f"    {domain:<35} {count:>6,}  ({pct:5.1f}%)")

    # ─── Verdict ─────────────────────────────────────────────────────────
    print(c("\n" + "=" * 72, Colors.CYAN))
    sendable_pct = (n_valid / n_has_email * 100) if n_has_email else 0

    if n_invalid == 0 and n_disposable == 0 and n_suspicious == 0:
        print(c("  ✅ VERDICT: GOOD TO SEND!", Colors.GREEN + Colors.BOLD))
        print(f"     {n_valid:,} valid emails ready ({sendable_pct:.1f}% of emails)")
        if n_empty > 0:
            print(c(f"     Note: {n_empty:,} records have no email (will be skipped)", Colors.DIM))
        if n_dup > 0:
            print(c(f"     Note: {n_dup:,} duplicate email records (consider deduplicating)", Colors.YELLOW))
        if n_typo > 0:
            print(c(f"     ⚠ {n_typo} possible domain typos found — review before sending", Colors.YELLOW))
    elif n_problematic < n_has_email * 0.05:
        print(c("  ⚠️  VERDICT: MOSTLY GOOD — minor issues found", Colors.YELLOW + Colors.BOLD))
        print(f"     {n_valid:,} valid emails ready ({sendable_pct:.1f}% of emails)")
        print(c(f"     {n_problematic:,} emails have issues — consider cleaning before send", Colors.YELLOW))
    else:
        print(c("  ❌ VERDICT: NEEDS CLEANING BEFORE SEND", Colors.RED + Colors.BOLD))
        print(f"     Only {n_valid:,} valid emails ({sendable_pct:.1f}% of emails)")
        print(c(f"     {n_problematic:,} emails have issues that need attention", Colors.RED))

    print(c("=" * 72, Colors.CYAN))
    print()


def export_clean_csv(results, output_file):
    """Export valid emails to a clean CSV file."""
    valid = results["valid"]
    if not valid:
        print(c("  No valid emails to export.", Colors.YELLOW))
        return

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ren_no", "full_name", "email", "mobile_no", "firm_name"])
        for entry in valid:
            rec = entry["record"]
            writer.writerow([
                rec.get("ren_no", ""),
                rec.get("full_name", "").strip(),
                rec.get("email", "").strip(),
                rec.get("mobile_no", ""),
                rec.get("firm_name", ""),
            ])

    print(c(f"  ✅ Exported {len(valid):,} valid emails to {output_file}", Colors.GREEN))


def save_report(results, output_file, do_dns=False):
    """Save a plain-text summary report."""
    total = results["total"]
    n_empty = len(results["empty_email"])
    n_has_email = total - n_empty

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Email Validation Report\n")
        f.write(f"{'=' * 60}\n")
        f.write(f"File: {INPUT_FILE}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total records:        {total:,}\n")
        f.write(f"With email:           {n_has_email:,}\n")
        f.write(f"Empty (no email):     {n_empty:,}\n")
        f.write(f"Valid & sendable:     {len(results['valid']):,}\n")
        f.write(f"Invalid format:       {len(results['invalid_format']):,}\n")
        f.write(f"Disposable domain:    {len(results['disposable']):,}\n")
        f.write(f"Typo in domain:       {len(results['typo_domain']):,}\n")
        f.write(f"Role-based:           {len(results['role_based']):,}\n")
        f.write(f"Suspicious:           {len(results['suspicious']):,}\n")
        f.write(f"Duplicate:            {len(results['duplicate']):,}\n")
        if do_dns:
            f.write(f"No MX record:         {len(results['no_mx']):,}\n")

        f.write(f"\n{'─' * 60}\nInvalid format emails:\n")
        for entry in results["invalid_format"]:
            f.write(f"  {entry['email']:<45} {entry['name']}\n")

        f.write(f"\n{'─' * 60}\nDomain typos:\n")
        for entry in results["typo_domain"]:
            suggested = entry.get("suggested_domain", "?")
            f.write(f"  {entry['email']:<45} → @{suggested}\n")

        f.write(f"\n{'─' * 60}\nSuspicious emails:\n")
        for entry in results["suspicious"]:
            f.write(f"  {entry['email']:<45} {entry['name']}\n")

        f.write(f"\n{'─' * 60}\nTop 20 domains:\n")
        for domain, count in results["domain_stats"].most_common(20):
            pct = count / n_has_email * 100 if n_has_email else 0
            f.write(f"  {domain:<35} {count:>6,}  ({pct:5.1f}%)\n")

    print(c(f"  📄 Report saved to {output_file}", Colors.CYAN))


# ─── Entry Point ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Validate emails in negotiator data")
    parser.add_argument("--dns", action="store_true", help="Enable MX record DNS checks (slower)")
    parser.add_argument("--export", action="store_true", help="Export clean emails to CSV")
    parser.add_argument("--file", default=INPUT_FILE, help="Input JSON file")
    args = parser.parse_args()

    input_file = args.file

    print(c("\n  📂 Loading data...", Colors.CYAN))
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(c(f"  ❌ File not found: {input_file}", Colors.RED))
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(c(f"  ❌ JSON parse error: {e}", Colors.RED))
        sys.exit(1)

    print(c(f"  ✅ Loaded {len(data):,} records", Colors.GREEN))

    print(c("\n  🔍 Validating emails...", Colors.CYAN))
    results = validate_emails(data, do_dns=args.dns)

    print_report(results, do_dns=args.dns)

    # Save plain text report
    save_report(results, OUTPUT_REPORT, do_dns=args.dns)

    # Export CSV if requested
    if args.export:
        export_clean_csv(results, OUTPUT_CSV)

    print()


if __name__ == "__main__":
    main()
