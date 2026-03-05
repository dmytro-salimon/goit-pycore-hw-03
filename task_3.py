import re

def normalize_phone(phone_number):
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    if cleaned.startswith('380'):
        return '+' + cleaned
    elif not cleaned.startswith('+'):
        return '+38' + cleaned
    return cleaned

if __name__ == "__main__":
    raw_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
    ]
    
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    for num in sanitized_numbers:
        print(num)