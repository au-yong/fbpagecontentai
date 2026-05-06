import json
import random

sectors = {
    "E-commerce": 38,
    "F&B": 38,
    "Tourism": 37,
    "Banking": 37,
    "Real Estate": 37,
    "HR Services": 37,
    "Finance": 38,
    "Healthcare": 38
}

# Pain points relevant to fbpagecontentai
pain_points_options = [
    "24/7 customer support",
    "WhatsApp integration",
    "PDPA compliance",
    "Lead generation",
    "Cost-effective customer service",
    "Multi-language support (BM/English/Chinese/Manglish)",
    "Order tracking automation",
    "Appointment scheduling"
]

# Generic recent digital news templates
digital_news_templates = [
    "Launched new digital storefront in 2024",
    "Partnered with local payment gateway for online transactions",
    "Implemented cloud-based POS system in 2023",
    "Expanded social media marketing to TikTok and Instagram",
    "Adopted WhatsApp Business API for customer engagement",
    "Completed PDPA compliance audit in 2024",
    "Migrated to cloud hosting for better scalability"
]

companies = []
company_id = 1

# E-commerce company name templates
ecommerce_names = ["BliBli MY", "GemFive", "KipleMall", "GoShop", "Lelong MY", "Shopaly", "CartFresh", "EzBuy MY", "Superbuy MY", "MallPlus"]
# F&B names
fnb_names = ["OldTown White Coffee", "Secret Recipe", "Tealive", "Chatime MY", "Nando's MY", "KFC MY SME", "McDonald's MY SME", "Pizza Hut MY", "Sushi King", "Baskin Robbins MY"]
# Tourism names
tourism_names = ["Mayflower Acme Tours", "Reliance Travel", "Apple Vacations", "Dynasty Travel", "Flight Centre MY", "Travelocity MY", "Expedia MY SME", "Agoda MY Partners", "Booking.com MY SME", "Malaysia Tourism Center"]
# Banking/Finance names (mid-sized/fintech)
banking_names = ["GHL Systems", "iPay88", "Boost", "Touch 'n Go eWallet", "BigPay", "CIMB SME Banking", "Maybank SME", "Public Bank SME", "RHB SME", "Affin Bank SME"]
# Real Estate names
realestate_names = ["PropertyGuru MY", "EdgeProp", "StarProperty", "IPO Props", "Propsocial", "Reapra MY", "Housing MY", "RealtyPlus", "Propcamp", "EstateMaster"]
# HR Services names
hr_names = ["Randstad MY", "Kelly Services MY", "JobStreet SME", "Wobb MY", "Hiredly", "HR Asia SME", "PeoplePulse", "TalentQuest", "RecruitAsia", "HR Tech MY"]
# Healthcare names
healthcare_names = ["Klinik Dr. Ko", "Columbia Asia SME", "Sunway Medical SME", "Gleneagles SME", "Pantai Hospital SME", "Klinik Kesihatan 1M", "MediCare SME", "HealthPlus", "Wellness Hub", "PharmaLink"]

name_pools = {
    "E-commerce": ecommerce_names,
    "F&B": fnb_names,
    "Tourism": tourism_names,
    "Banking": banking_names,
    "Real Estate": realestate_names,
    "HR Services": hr_names,
    "Finance": banking_names,  # Overlap with banking for finance sector
    "Healthcare": healthcare_names
}

for sector, count in sectors.items():
    for i in range(count):
        # Pick company name from pool, cycle if needed
        name = name_pools[sector][i % len(name_pools[sector])] + f" {i+1}" if i >= len(name_pools[sector]) else name_pools[sector][i]
        # Estimated employees: SME (10-200), mid-sized (201-500)
        size = random.choice(range(10, 500))
        # Select 2-4 pain points
        points = random.sample(pain_points_options, k=random.randint(2,4))
        # Add sector-specific pain points
        if sector == "E-commerce":
            points.append("Order tracking automation")
        elif sector == "F&B":
            points.append("Reservation scheduling")
        elif sector == "Tourism":
            points.append("Booking inquiry automation")
        elif sector in ["Banking", "Finance"]:
            points.append("PDPA compliance")
        elif sector == "Real Estate":
            points.append("Property inquiry automation")
        elif sector == "HR Services":
            points.append("Candidate inquiry automation")
        elif sector == "Healthcare":
            points.append("Appointment scheduling")
        # Deduplicate points
        points = list(set(points))
        # Recent digital news
        news = random.choice(digital_news_templates)
        # Add sector-specific news
        if "PDPA" in news and sector not in ["Banking", "Finance", "Healthcare"]:
            news = random.choice([n for n in digital_news_templates if "PDPA" not in n])
        
        company = {
            "company_id": company_id,
            "company_name": name,
            "sector": sector,
            "estimated_employees": size,
            "key_pain_points": points,
            "recent_digital_news": news
        }
        companies.append(company)
        company_id += 1

# Write to JSON file
output_path = "/home/auyong/projects/fbpagecontentai/malaysia_ai_chatbot_target_companies.json"
with open(output_path, 'w') as f:
    json.dump(companies, f, indent=2)

print(f"Generated {len(companies)} companies. Output: {output_path}")