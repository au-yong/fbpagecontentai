import json
import csv

# File paths
input_file = "lpeph_negotiators_20260505_010015.json"
output_file = "output_audience.csv"

CURRENT_YEAR = 2026

def parse_nric(nric):
    if not nric or len(nric) < 12:
        return "", "", "", ""
    
    yy = nric[0:2]
    mm = nric[2:4]
    dd = nric[4:6]
    last_digit = nric[-1]
    
    try:
        yy_int = int(yy)
        year = 1900 + yy_int if yy_int > 26 else 2000 + yy_int
        doby = str(year)
        dob = f"{int(mm)}/{int(dd)}/{yy}"
        age = str(CURRENT_YEAR - year)
        gen = "M" if int(last_digit) % 2 != 0 else "F"
        return dob, doby, gen, age
    except ValueError:
        return "", "", "", ""

def parse_name(full_name):
    if not full_name:
        return "", ""
    
    # Clean string and remove quotes
    full_name = full_name.replace('"', '').replace("'", '').strip()
    parts = full_name.split()
    
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    
    return parts[0], " ".join(parts[1:])

def format_phone(phone):
    if not phone:
        return ""
    phone = phone.strip().replace("-", "").replace(" ", "").replace("+", "")
    if phone.startswith("0"):
        phone = "6" + phone
    return phone

def main():
    print(f"Loading data from {input_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    # Headers according to example_value_based_audience_file.csv
    headers = [
        "email", "email", "email", 
        "phone", "phone", "phone", 
        "madid", "fn", "ln", "zip", 
        "ct", "st", "country", 
        "dob", "doby", "gen", "age", "uid", "value"
    ]
    
    print(f"Writing to {output_file}...")
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            
            for row in data:
                email = row.get("email", "").strip() if row.get("email") else ""
                phone = format_phone(row.get("mobile_no", ""))
                
                fn, ln = parse_name(row.get("full_name", ""))
                
                dob, doby, gen, age = parse_nric(row.get("nric_no", ""))
                
                uid = row.get("ren_no", "") if row.get("ren_no") else ""
                
                # Fill in the row based on available data
                csv_row = [
                    email, "", "", # 3 email columns, using first for primary
                    phone, "", "", # 3 phone columns, using first for primary
                    "", # madid
                    fn, ln, # first name, last name
                    "", "", "", # zip, ct, st
                    "MY", # country
                    dob, doby, gen, age, # dob, doby, gen, age extracted from NRIC
                    uid, # uid
                    "" # value
                ]
                writer.writerow(csv_row)
                
        print(f"Successfully processed {len(data)} records to {output_file}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == "__main__":
    main()
