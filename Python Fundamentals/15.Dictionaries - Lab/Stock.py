elements = input().split(" ")
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]

    bakery[key] = int(value)

searched_products = input().split(" ")

for k in searched_products:
    if k in bakery:
        print(f"We have {bakery[k]} of {k} left")
    else:
        print(f"Sorry, we don't have {k}")
