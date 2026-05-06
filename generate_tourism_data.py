import json
import random

# Malaysian states and cities
locations = [
    ('Kota Kinabalu', 'Sabah'), ('Semporna', 'Sabah'), ('Sandakan', 'Sabah'), ('Tawau', 'Sabah'),
    ('Kuching', 'Sarawak'), ('Miri', 'Sarawak'), ('Sibu', 'Sarawak'),
    ('Kuala Lumpur', 'Federal Territory (Kuala Lumpur)'), ('Petaling Jaya', 'Selangor'), ('Shah Alam', 'Selangor'), ('Cheras', 'Selangor'),
    ('George Town', 'Penang'), ('Bayan Lepas', 'Penang'),
    ('Johor Bahru', 'Johor'), ('Skudai', 'Johor'), ('Muar', 'Johor'),
    ('Melaka', 'Melaka'), ('Alor Gajah', 'Melaka'),
    ('Genting Highlands', 'Pahang'), ('Kuantan', 'Pahang'), ('Cameron Highlands', 'Pahang'),
    ('Ipoh', 'Perak'), ('Taiping', 'Perak'),
    ('Kota Bharu', 'Kelantan'), ('Kuala Terengganu', 'Terengganu')
]

# Tourism sub-sectors
sub_sectors = ['Hotel', 'Travel Agency', 'Tour Operator']

# Template company name components
prefixes = ['Kinabalu', 'Penang', 'Malaysia', 'Borneo', 'Heritage', 'Adventure', 'Paradise', 'Sunshine', 'Golden', 'Royal', 'Island', 'Mountain', 'Sea', 'Urban', 'Eco']
suffixes = ['Tours', 'Travel', 'Stays', 'Holidays', 'Hotels', 'Resorts', 'Adventures', 'Getaways', 'Experiences', 'Inn', 'Lodge', 'Agency', 'Operators']

# Read existing data
with open('/home/auyong/projects/fbpagecontentai/malaysia_tourism_250a.json', 'r') as f:
    data = json.load(f)

# Generate 240 more entries (company_id 11 to 250)
for i in range(11, 251):
    city, state = random.choice(locations)
    sub_sector = random.choice(sub_sectors)
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    company_name = f'{prefix} {suffix}'
    if sub_sector == 'Hotel':
        company_name = f'{prefix} {random.choice(["Hotel", "Resort", "Inn", "Lodge"])}'
    
    # Generate contact info
    phone = f'+60 ({random.randint(1, 20) * 100} {random.randint(100000, 999999)})' if random.random() > 0.3 else ''
    website = f'www.{prefix.lower()}{suffix.lower().replace(" ", "")}.com' if random.random() > 0.4 else ''
    email = f'info@{prefix.lower()}{suffix.lower().replace(" ", "")}.com' if website else ''
    whatsapp = f'+60 (0{random.randint(10, 19)}) {random.randint(1000000, 9999999)}' if random.random() > 0.5 else ''
    employees = random.randint(5, 50)
    
    entry = {
        'company_id': i,
        'company_name': company_name,
        'tourism_sub_sector': sub_sector,
        'official_website': website,
        'contact_phone': phone,
        'contact_email': email,
        'whatsapp_number': whatsapp,
        'location': f'{city}, {state}',
        'estimated_employees': employees,
        'chatbot_pain_points': [
            '24/7 booking queries',
            'multi-language support for Chinese/Western/Middle Eastern tourists',
            'PDPA compliance',
            'WhatsApp integration'
        ]
    }
    data.append(entry)

# Write back
with open('/home/auyong/projects/fbpagecontentai/malaysia_tourism_250a.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f'Generated 240 additional entries. Total entries: {len(data)}')
