import json

# Load first batch (list format)
with open('malaysia_tourism_250a.json', 'r') as f:
    batch_a = json.load(f)  # This is a list

# Load second batch (dict with 'companies' key)
with open('malaysia_tourism_250b.json', 'r') as f:
    batch_b_dict = json.load(f)
    batch_b = batch_b_dict['companies']  # Extract the list

# Combine
combined = batch_a + batch_b

# Reassign company_ids 1-500
for i, company in enumerate(combined, 1):
    company['company_id'] = i

# Write combined file
with open('malaysia_tourism_top500_companies.json', 'w') as f:
    json.dump(combined, f, indent=2)

print(f'Successfully combined {len(combined)} companies into malaysia_tourism_top500_companies.json')
