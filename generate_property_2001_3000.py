import json
import random

# Name pools for property agents
residential_names = ["KL Residential Pro", "Penang Home Finders", "Johor Bahru Housing", "Subang Property Hub", 
                     "Shah Alam House Hunt", "Petaling Jaya Homes", "Klang Valley Properties", "Bangsar Residential",
                     "Mont Kiara Living", "Damansara Realty", "Cheras Property Plus", "Ampang Home Search"]

commercial_names = ["KL Commercial Hub", "Penang Biz Properties", "Johor Industrial Zone", "Shah Alam Office Space",
                    "Subang Business Park", "Petaling Jaya Commercial", "Klang Commercial Pro", "Bangsar Office Tower",
                    "Mont Kiara Suites", "Damansara Business", "Cheras Commercial", "Ampang Plaza Properties"]

luxury_names = ["Luxury Living KL", "Elite Penang Properties", "Premium Johor Homes", "Exclusive Subang Realty",
                "Prestige Shah Alam", "Grand Petaling Jaya", "Royal Klang Valley", "Signature Bangsar",
                "Platinum Mont Kiara", "Diamond Damansara", "Gold Cheras Properties", "Supreme Ampang Realty"]

property_types = ['real_estate_agency', 'property_consultant', 'luxury_property', 'residential_commercial']

locations = [
    ("Kota Kinabalu", "Sabah"), ("Kuala Lumpur", "Federal Territory"), ("Penang", "Penang"), 
    ("Johor Bahru", "Johor"), ("Shah Alam", "Selangor"), ("Petaling Jaya", "Selangor"),
    ("Malacca City", "Malacca"), ("Ipoh", "Perak"), ("Kuching", "Sarawak"), ("Klang", "Selangor"),
    ("Subang Jaya", "Selangor"), ("Bangsar", "Federal Territory"), ("Mont Kiara", "Federal Territory"),
    ("Damansara", "Selangor"), ("Cheras", "Federal Territory"), ("Ampang", "Federal Territory")
]

def generate_agent(agent_id):
    sub_sector = random.choice(property_types)
    
    if sub_sector == 'real_estate_agency':
        name = random.choice(residential_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['5-10', '10-20', '20-50'])
    elif sub_sector == 'property_consultant':
        name = random.choice(commercial_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['3-8', '8-15', '15-30'])
    elif sub_sector == 'luxury_property':
        name = random.choice(luxury_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['5-15', '15-30', '30-50'])
    else:
        name = random.choice(residential_names + commercial_names) + " " + str(random.randint(1, 99))
        employees = random.choice(['10-30', '30-50', '50-100'])
    
    location = random.choice(locations)
    phone = f"+60 {random.randint(10, 19)}-{random.randint(100, 999)} {random.randint(1000, 9999)}"
    whatsapp = f"+601{random.randint(0,9)}-{random.randint(1000, 9999)}"
    email_name = name.lower().replace(' ', '').replace('\'', '')
    
    pain_points = random.sample([
        "24/7 property inquiries",
        "appointment scheduling for viewings",
        "multi-language for foreign investors",
        "PDPA compliance for client data",
        "WhatsApp integration",
        "lead qualification"
    ], k=random.randint(3, 6))
    
    return {
        "company_id": agent_id,
        "company_name": name,
        "property_sub_sector": sub_sector,
        "official_website": f"www.{email_name}.com.my",
        "contact_phone": phone,
        "contact_email": f"contact@{email_name}.com.my",
        "whatsapp_number": whatsapp,
        "location": f"{location[0]}, {location[1]}",
        "estimated_employees": employees,
        "chatbot_pain_points": pain_points
    }

# Generate batch 4: IDs 2001-2500
batch4 = [generate_agent(i) for i in range(2001, 2501)]
with open('/home/auyong/projects/fbpagecontentai/malaysia_property_2001_2500.json', 'w') as f:
    json.dump(batch4, f, indent=2)
print(f"Generated batch 4: {len(batch4)} agents (IDs 2001-2500)")

# Generate batch 5: IDs 2501-3000
batch5 = [generate_agent(i) for i in range(2501, 3001)]
with open('/home/auyong/projects/fbpagecontentai/malaysia_property_2501_3000.json', 'w') as f:
    json.dump(batch5, f, indent=2)
print(f"Generated batch 5: {len(batch5)} agents (IDs 2501-3000)")
