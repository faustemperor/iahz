import re

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[@#$%&]', password))
    return has_upper and has_lower and has_digit and has_special

print(is_strong_password("Passw0rd@"))
print(is_strong_password("weakpass"))