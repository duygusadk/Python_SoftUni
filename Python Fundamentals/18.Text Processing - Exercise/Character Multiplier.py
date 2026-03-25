first, second = input().split()
total_sum = 0

if len(first) > len(second):
    for i in range(len(second)):
        total_sum += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        total_sum += ord(first[i])
elif len(first) < len(second):
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        total_sum += ord(second[i])
else:
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])

print(total_sum)
