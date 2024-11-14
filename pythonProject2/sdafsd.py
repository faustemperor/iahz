import re

def replace_prices(text: str) -> str:
    pattern = r'\b(\d+)\s*(руб\.?|рубля)\b'
    return re.sub(pattern, "PRICE", text)
text = "Цена ноутбука 50000 руб., а телефона - 2000 рубля."

print(replace_prices(text))