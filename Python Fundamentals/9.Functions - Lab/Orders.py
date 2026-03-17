product = input()
n = int(input())


def total(product, n):
    if product == 'coffee':
        return 1.50 * n
    elif product == 'water':
        return 1.00 * n
    elif product == 'coke':
        return 1.40 * n
    elif product == 'snacks':
        return 2.00 * n


print(f"{total(product, n):.2f}")
