import json
import re
import os

# Common Chinese surnames in Malaysia (transliterated)
CHINESE_SURNAMES = {
    'TAN', 'LIM', 'LEE', 'WONG', 'NG', 'CHAN', 'CHONG', 'YONG', 'CHEE', 'LOH',
    'YEOH', 'CHENG', 'LOW', 'HO', 'TEOH', 'TEO', 'CHIA', 'ANG', 'LAU', 'KOH',
    'LIEW', 'CHOO', 'KHOO', 'SIM', 'GAN', 'CHAW', 'CHENG', 'CHEONG', 'CHEW',
    'CHIN', 'CHU', 'FONG', 'FOO', 'HEW', 'HII', 'KOAY', 'KONG', 'KUA', 'KUAN',
    'KWOK', 'LAM', 'LAU', 'LEE', 'LEONG', 'LIAN', 'LIEW', 'LIM', 'LING', 'LO',
    'LOH', 'LOKE', 'LOO', 'LOW', 'LUM', 'MA', 'NEOH', 'NG', 'NGEOW', 'OCK',
    'ONG', 'OOI', 'PANG', 'PHANG', 'PHUA', 'POON', 'QUAH', 'SAM', 'SAW', 'SEOW',
    'SIA', 'SIEW', 'SIM', 'SIN', 'SOO', 'SOON', 'SUN', 'TAI', 'TAN', 'TANG',
    'TAY', 'TEE', 'TEH', 'TENG', 'TEO', 'TEOH', 'THAM', 'THIEN', 'TING', 'TOH',
    'TSAI', 'WEE', 'WONG', 'WOO', 'YAP', 'YAU', 'YEO', 'YEOH', 'YEOW', 'YIP',
    'YONG', 'YOONG'
}

# Markers for Malay and Indian names
NON_CHINESE_MARKERS = {'BIN', 'BINTI', 'AL', 'AP', 'ABD', 'ABDU', 'MOHD', 'MUHAMMAD'}

def is_chinese_name(name):
    if not name:
        return False
    
    name = name.strip().upper()
    
    # 1. Check for actual Chinese characters
    if re.search(r'[\u4e00-\u9fff]', name):
        return True
    
    # 2. Check for Non-Chinese markers first
    # (e.g. "MOHD BIN TAN" should be English content if it's a Malay name)
    # Note: "TAN" is also a Malay name in some regions, but rare compared to Chinese.
    parts = re.split(r'[^A-Z]', name)
    parts = [p for p in parts if p]
    
    if any(marker in parts for marker in NON_CHINESE_MARKERS):
        return False
    
    # 3. Check for Chinese-sounding name (heuristic)
    if not parts:
        return False
    
    # Check if any part is a common Chinese surname
    for part in parts:
        if part in CHINESE_SURNAMES:
            return True
            
    return False

def calculate_age(nric):
    if not nric or not isinstance(nric, str):
        return None
    
    # Clean NRIC (remove dashes/spaces)
    nric = re.sub(r'\D', '', nric)
    
    if len(nric) < 2:
        return None
        
    try:
        year_suffix = int(nric[:2])
        # Assume 2026 as current year
        current_year = 2026
        current_year_suffix = current_year % 100
        
        if year_suffix <= current_year_suffix:
            birth_year = 2000 + year_suffix
        else:
            birth_year = 1900 + year_suffix
            
        return current_year - birth_year
    except:
        return None

def main():
    json_path = 'lpeph_negotiators_20260505_010015.json'
    output_path = 'lpeph_negotiators_classified.json'
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    print(f"Processing {len(data)} records...")
    
    chinese_count = 0
    english_count = 0
    email_count = 0
    
    classified_data = []
    
    for record in data:
        name = record.get('full_name', '')
        nric = record.get('nric_no', '')
        
        # 1. Classify language
        if is_chinese_name(name):
            record['content_language'] = 'Chinese'
            chinese_count += 1
        else:
            record['content_language'] = 'English'
            english_count += 1
            
        # 2. Calculate age
        record['age'] = calculate_age(nric)
        
        # 3. Check for email
        email = record.get('email', '')
        if email and isinstance(email, str) and '@' in email:
            email_count += 1
            
        classified_data.append(record)

    print(f"Results:")
    print(f"  Chinese content recipients: {chinese_count}")
    print(f"  English content recipients: {english_count}")
    print(f"  Records with email: {email_count}")
    
    print(f"Saving to {output_path}...")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(classified_data, f, indent=2)
        print("Done!")
    except Exception as e:
        print(f"Error saving JSON: {e}")

if __name__ == "__main__":
    main()
