import re

n = int(input())

regex = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
code = ''
isDigits = False
for i in range(n):
    text = input()
    matches = re.findall(regex, text)
    if not matches:
        print("Invalid barcode")
        continue
    for product in matches:
        for ch in product[1]:
            if ch.isdigit():
                code = code + ch
                isDigits = True
        if not isDigits:
            code = '00'
        print(f"Product group: {code}")
        code = ""
        isDigits = False
