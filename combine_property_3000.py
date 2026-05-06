import json

# Load all 6 batches
with open('malaysia_property_agents_500.json', 'r') as f:
    batch1 = json.load(f)  # IDs 1-500

with open('malaysia_property_501_1000.json', 'r') as f:
    batch2 = json.load(f)  # IDs 501-1000

with open('malaysia_property_1001_1500.json', 'r') as f:
    batch3 = json.load(f)  # IDs 1001-1500

with open('malaysia_property_1501_2000.json', 'r') as f:
    batch4 = json.load(f)  # IDs 1501-2000

with open('malaysia_property_2001_2500.json', 'r') as f:
    batch5 = json.load(f)  # IDs 2001-2500

with open('malaysia_property_2501_3000.json', 'r') as f:
    batch6 = json.load(f)  # IDs 2501-3000

# Combine all batches
combined = batch1 + batch2 + batch3 + batch4 + batch5 + batch6

print(f"Total agents before reassign: {len(combined)}")

# Verify and reassign IDs sequentially
for i, agent in enumerate(combined, 1):
    agent['company_id'] = i

print(f"Total agents after combining: {len(combined)}")
print(f"ID range: {combined[0]['company_id']} to {combined[-1]['company_id']}")

# Write final combined file
with open('malaysia_property_agents_3000.json', 'w') as f:
    json.dump(combined, f, indent=2)

print(f"Successfully created malaysia_property_agents_3000.json with {len(combined)} property agents")
