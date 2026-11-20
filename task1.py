def check_subsidy_separate(units, has_ration_card, has_member_above_80):
    subsidy_given = False
    
    if units <= 100:
        subsidy_given = True
    if 101 <= units <= 200 and has_ration_card:
        subsidy_given = True
    if units > 200 and has_member_above_80:
        subsidy_given = True
        
    return subsidy_given

def check_subsidy_elif(units, has_ration_card, has_member_above_80):
    if units <= 100:
        return True
    elif 101 <= units <= 200:
        return has_ration_card
    else:
        return has_member_above_80

households = [
    {"units": 50, "ration_card": False, "age_80": False},
    {"units": 100, "ration_card": False, "age_80": False},
    {"units": 101, "ration_card": False, "age_80": False},
    {"units": 101, "ration_card": True, "age_80": False},
    {"units": 175, "ration_card": True, "age_80": False},
    {"units": 200, "ration_card": False, "age_80": False},
    {"units": 201, "ration_card": True, "age_80": False},
    {"units": 250, "ration_card": False, "age_80": True}
]

print("--- Separate If Statements ---")
for i, h in enumerate(households, 1):
    res = check_subsidy_separate(h["units"], h["ration_card"], h["age_80"])
    print(f"Household {i} (Units: {h['units']}, Ration Card: {h['ration_card']}, Age > 80: {h['age_80']}) -> Subsidy: {res}")

print("\n--- If-Elif-Else Statement ---")
for i, h in enumerate(households, 1):
    res = check_subsidy_elif(h["units"], h["ration_card"], h["age_80"])
    print(f"Household {i} (Units: {h['units']}, Ration Card: {h['ration_card']}, Age > 80: {h['age_80']}) -> Subsidy: {res}")
