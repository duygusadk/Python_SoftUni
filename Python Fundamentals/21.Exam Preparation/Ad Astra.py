import re

text = input()
pattern = r"(?i)([|#])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern, text)

total_calories = sum([int(calories[3]) for calories in matches])
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for i in matches:
    item_name = i[1]
    expiration_date = i[2]
    calories = i[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
