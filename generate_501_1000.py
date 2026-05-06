import json
import random

# Name pools by sub-sector
hotel_names = ["Kinabalu View Lodge", "Penang Heritage Homestay", "Desaru Beach Resort", "Langkawi Coral Bay", "Cameron Tea Garden Inn", 
                "Tioman Reef Resort", "Redang Island Lodge", "Pangkor Palm Beach", "Perhentian Blue Water", "Mabul Sipadan Dive",
                "Borneo Rainforest Lodge", "Highland Pine Resort", "Jungle River Camp", "Mangrove Eco Stay", "Orchard Country Inn",
                "Seaview Budget Hotel", "Golden Sands Hotel", "Sunrise Beach Chalet", "Palm Grove Resort", "Coconut Bay Inn"]

homestay_names = ["Kampung Style Homestay", "Traditional Malay House", "Heritage Wooden Home", "Orchard Homestay", "Paddy Field Stay",
                   "Village Life Homestay", "Riverside Wooden Hut", "Mountain View Homestay", "Garden City Homestay", "Coastal Breeze Stay",
                   "Cultural Heritage Home", "Ancient House Stay", "Colonial Bungalow", "Modern Family Home", "Budget Friendly Stay"]

resort_names = ["Sunset Bay Resort", "Crystal Waters Resort", "Emerald Valley Resort", "Paradise Found Resort", "Serenity Beach Resort",
                "Tropical Paradise Resort", "Golden Horizon Resort", "Royal Palm Resort", "Lagoon View Resort", "Coral Reef Resort",
                "Mountain Mist Resort", "Forest Edge Resort", "Lake Side Resort", "River Valley Resort", "Starlight Beach Resort"]

lodge_names = ["Jungle Safari Lodge", "Rainforest Canopy Lodge", "Eco Adventure Lodge", "Wildlife Safari Lodge", "Nature's Nest Lodge",
               "Canopy Walk Lodge", "Tree Top Lodge", "River Safari Lodge", "Forest Canopy Lodge", "Mountain Stream Lodge"]

locations = [
    ("Kota Kinabalu", "Sabah"), ("Kuala Lumpur", "Federal Territory"), ("Penang", "Penang"), ("Langkawi", "Kedah"),
    ("Johor Bahru", "Johor"), ("Kuching", "Sarawak"), ("Ipoh", "Perak"), ("Shah Alam", "Selangor"),
    ("Malacca City", "Malacca"), ("Cameron Highlands", "Pahang"), ("Genting Highlands", "Pahang"), ("Tioman Island", "Pahang"),
    ("Redang Island", "Terengganu"), ("Pangkor Island", "Perak"), ("Miri", "Sarawak"), ("Sandakan", "Sabah"),
    ("Tawau", "Sabah"), ("Labuan", "Federal Territory"), ("Seremban", "Negeri Sembilan"), ("Kuantan", "Pahang")
]

def generate_company(company_id):
    sub_sector = random.choice(['hotel', 'homestay', 'resort', 'lodge'])
    
    if sub_sector == 'hotel':
        name = random.choice(hotel_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['10-30', '30-50', '50-100'])
    elif sub_sector == 'homestay':
        name = random.choice(homestay_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['2-5', '5-10', '10-20'])
    elif sub_sector == 'resort':
        name = random.choice(resort_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['50-100', '100-200', '200-500'])
    else:  # lodge
        name = random.choice(lodge_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['10-30', '30-50', '50-100'])
    
    location = random.choice(locations)
    phone = f"+60 {random.randint(10, 19)}-{random.randint(100, 999)} {random.randint(1000, 9999)}"
    whatsapp = f"+601{random.randint(0,9)}-{random.randint(1000, 9999)}"
    
    pain_points = random.sample([
        "24/7 booking queries",
        "multi-language support for Chinese/Western/Middle Eastern tourists",
        "PDPA compliance",
        "WhatsApp integration",
        "itinerary assistance",
        "24/7 guest support"
    ], k=random.randint(2, 4))
    
    return {
        "company_id": company_id,
        "company_name": name,
        "tourism_sub_sector": sub_sector,
        "official_website": f"www.{name.lower().replace(' ', '').replace('\'', '')}.com.my",
        "contact_phone": phone,
        "contact_email": f"info@{name.lower().replace(' ', '').replace('\'', '')}.com.my",
        "whatsapp_number": whatsapp,
        "location": f"{location[0]}, {location[1]}",
        "estimated_employees": employees,
        "chatbot_pain_points": pain_points
    }

# Generate 500 companies (IDs 501-1000)
companies = [generate_company(i) for i in range(501, 1001)]

# Write to file
with open('/home/auyong/projects/fbpagecontentai/malaysia_tourism_501_1000.json', 'w') as f:
    json.dump(companies, f, indent=2)

print(f"Generated {len(companies)} companies (IDs 501-1000)")
