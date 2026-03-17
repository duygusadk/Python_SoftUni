n = int(input())
sum = 0
for i in range(1, n + 1):
    litters = int(input())

    if sum + litters > 255:
        print("Insufficient capacity!")
        continue

    sum += litters
print(sum)
