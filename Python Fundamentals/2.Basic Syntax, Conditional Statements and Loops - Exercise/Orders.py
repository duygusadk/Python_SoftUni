n = int(input())

total_price = 0
for i in range(n):

    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())

    if 0.01 <= price_per_capsule <= 100.0 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        price = capsules * days * price_per_capsule
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price

print(f"Total: ${total_price:.2f}")
