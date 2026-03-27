import re

bought_furniture = []
total_cost = 0
regex = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
text = input()
while text != "Purchase":

    matches = re.search(regex, text,re.IGNORECASE)
    if matches:
        name, price, quantity = matches.groups()
        bought_furniture.append(name)
        total_cost += float(price) * int(quantity)
    text = input()

print("Bought furniture:")
for i in bought_furniture:
    print(i)
print(f"Total money spend: {total_cost:.2f}")
