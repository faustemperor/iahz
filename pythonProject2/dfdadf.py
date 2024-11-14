import re

def extract_hashtags(text: str) -> list:
    pattern = r'#\w+'
    return re.findall(pattern, text)
text = "Сегодня отличный день! #python #programming #100DaysOfCode"

print(extract_hashtags(text))