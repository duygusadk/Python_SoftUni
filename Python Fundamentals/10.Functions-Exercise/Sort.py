string_numbers = input().split()
numbers = []

for i in string_numbers:
    numbers.append(int(i))

numbers.sort()
print(numbers)