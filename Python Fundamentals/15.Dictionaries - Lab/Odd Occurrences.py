info = input().split()

sequence = {}

for i in info:
    if i.lower() not in sequence.keys():
        sequence[i.lower()] = 0
    sequence[i.lower()] += 1

for key,value in sequence.items():
    if value % 2 != 0:
        print(key, end=" ")
