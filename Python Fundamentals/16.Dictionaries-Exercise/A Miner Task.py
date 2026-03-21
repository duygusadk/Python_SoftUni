resource = input()
count = 0

resources = {}
while resource != "stop":
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = quantity
    else:
        resources[resource] += quantity

    resource = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
