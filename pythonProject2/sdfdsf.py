import re

def split_by_sentence(text: str) -> list:
    return re.split(r'(?<=[.!?]) +', text.strip())
text = "Привет! Как дела? Все хорошо..."

print(split_by_sentence(text))