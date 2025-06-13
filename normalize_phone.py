import re

def normalize_phone_number(phone_number):
    # Remove all characters except numbers and the '+' sign
    normalized = re.sub(r'[^\d+]', '', phone_number)

    if normalized.startswith('+'):
        pass
    elif normalized.startswith('38'):
        normalized = '+' + normalized
    else:
        normalized = '+38' + normalized

    return normalized

print(normalize_phone_number("067\\t123 4567")) #+380671234567  
print(normalize_phone_number("(095) 234-5678\\n")) # +380952345678
print(normalize_phone_number("+380 44 123 4567"))  # +380501234567
print(normalize_phone_number("380501234567"))  # +380501234567
print(normalize_phone_number("    +38(050)123-32-34"))  # +38050123234
print(normalize_phone_number("     0503451234"))  # +380503451234
print(normalize_phone_number("(050)8889900"))  # +380508889900
print(normalize_phone_number("38050-111-22-22"))  # +380501112222
print(normalize_phone_number("38050 111 22 11   "))  # +380501112211
