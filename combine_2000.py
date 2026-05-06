import json

# Load all 4 batches
with open('malaysia_tourism_top500_companies.json', 'r') as f:
    batch1 = json.load(f)  # IDs 1-500

with open('malaysia_tourism_501_1000.json', 'r') as f:
    batch2 = json.load(f)  # IDs 501-1000

with open('malaysia_tourism_1001_1500.json', 'r') as f:
    batch3 = json.load(f)  # IDs 1001-1500

with open('malaysia_tourism_1501_2000.json', 'r') as f:
    batch4 = json.load(f)  # IDs 1501-2000

# Combine all batches
combined = batch1 + batch2 + batch3 + batch4

# Verify count and reassign IDs sequentially
print(f"Total companies before reassign: {len(combined)}")
for i, company in enumerate(combined, 1):
    company['company_id'] = i

print(f"Total companies after combining: {len(combined)}")

# Write final combined file
with open('malaysia_tourism_top2000_companies.json', 'w') as f:
    json.dump(combined, f, indent=2)

print(f"Successfully created malaysia_tourism_top2000_companies.json with {len(combined)} companies")
print(f"ID range: {combined[0]['company_id']} to {combined[-1]['company_id']}")
