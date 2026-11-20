def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
    # TODO 1: Remove spaces and hyphens and convert to upper case using string methods
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
    # TODO 2: Check the length is 9 or 10, then check each part using slicing with
    # isalpha() and isdigit()
    length = len(reg)
    if length not in (9, 10):
        return False
    
    state = reg[:2]
    district = reg[2:4]
    if length == 9:
        series = reg[4:5]
        digits = reg[5:]
    else:
        series = reg[4:6]
        digits = reg[6:]
        
    return state.isalpha() and district.isdigit() and series.isalpha() and digits.isdigit()

def format_number(reg):
    if not is_valid(reg):
        return "INVALID"
    length = len(reg)
    if length == 9:
        return f"{reg[:2]} {reg[2:4]} {reg[4:5]} {reg[5:]}"
    else:
        return f"{reg[:2]} {reg[2:4]} {reg[4:6]} {reg[6:]}"

for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")
