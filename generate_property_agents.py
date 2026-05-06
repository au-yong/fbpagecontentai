import json
import random

# Malaysian states and major cities
locations = [
    ("Kuala Lumpur", "Kuala Lumpur"),
    ("George Town", "Penang"),
    ("Johor Bahru", "Johor"),
    ("Shah Alam", "Selangor"),
    ("Petaling Jaya", "Selangor"),
    ("Ipoh", "Perak"),
    ("Kota Kinabalu", "Sabah"),
    ("Kuching", "Sarawak"),
    ("Melaka", "Melaka"),
    ("Seremban", "Negeri Sembilan"),
    ("Alor Setar", "Kedah"),
    ("Kuantan", "Pahang"),
    ("Kuala Terengganu", "Terengganu"),
    ("Kangar", "Perlis"),
    ("Sandakan", "Sabah"),
    ("Miri", "Sarawak"),
    ("Batu Pahat", "Johor"),
    ("Segamat", "Johor"),
    ("Taiping", "Perak"),
    ("Teluk Intan", "Perak")
]

# Property sub-sectors
sub_sectors = ["real_estate_agency", "property_consultant", "luxury_property", "residential_commercial"]

# Agency name templates
agency_templates = [
    "{city} Property Hub",
    "{city} Realty Group",
    "{state} Land & Homes",
    "Prime {city} Properties",
    "{city} Estate Agents",
    "Golden {state} Realty",
    "Metro {city} Homes",
    "{state} Property Consultants",
    "Elite {city} Real Estate",
    "Heritage {city} Properties"
]

# Chatbot pain points (all common for property agencies)
pain_points = [
    "24/7 property inquiries",
    "appointment scheduling for viewings",
    "multi-language for foreign investors",
    "PDPA compliance for client data",
    "WhatsApp integration",
    "lead qualification"
]

# Generate 500 entries
agents = []
for i in range(1, 501):
    # Select random location
    city, state = random.choice(locations)
    # Generate agency name
    template = random.choice(agency_templates)
    company_name = template.format(city=city, state=state)
    # Ensure unique names by adding number if needed (simplified, assume unique for this template)
    # Select sub-sector
    property_sub_sector = random.choice(sub_sectors)
    # Generate contact details
    # Phone: +60 12/13/14/15/16/17/18/19 xxxx xxxx
    prefix = random.choice(["12", "13", "14", "15", "16", "17", "18", "19"])
    phone = f"+60 {prefix} {random.randint(1000,9999)} {random.randint(1000,9999)}"
    # Email: contact@agencyname.com (simplified, replace spaces/special chars)
    email_local = company_name.lower().replace(" ", "").replace("&", "and")[:20]
    contact_email = f"contact@{email_local}.com"
    # WhatsApp: same as phone (common in Malaysia)
    whatsapp_number = phone
    # Official website
    website = f"https://www.{email_local}.com"
    # Estimated employees: 1-50 (typical for SME agencies)
    estimated_employees = random.randint(1, 50)
    # Location
    location = f"{city}/{state}"
    
    agent = {
        "company_id": i,
        "company_name": company_name,
        "property_sub_sector": property_sub_sector,
        "official_website": website,
        "contact_phone": phone,
        "contact_email": contact_email,
        "whatsapp_number": whatsapp_number,
        "location": location,
        "estimated_employees": estimated_employees,
        "chatbot_pain_points": pain_points.copy()
    }
    agents.append(agent)

# Write to JSON file
output_path = "/home/auyong/projects/fbpagecontentai/malaysia_property_agents_500.json"
with open(output_path, "w") as f:
    json.dump(agents, f, indent=2, ensure_ascii=False)

print(f"Generated 500 property agent entries to {output_path}")
