command = input()

orders = {}
total_quantity = 0
while command != "buy":
    info = command.split()
    name, price, quantity = info[0], float(info[1]), int(info[2])

    if name not in orders.keys():
        orders[name] = {}
        orders[name][price] = quantity

    else:
        total_quantity = list(orders[name].values())[0]
        total_quantity += quantity
        orders[name].clear()

        orders[name][price] = total_quantity

    command = input()

for key, value in orders.items():
    for price, quantity in value.items():
        print(f"{key} -> {price * quantity:.2f}")
