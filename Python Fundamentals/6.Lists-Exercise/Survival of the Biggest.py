string_numbers = input().split()
numbers = []
n = int(input())
new_list = []
for num in string_numbers:
    numbers.append(int(num))

for i in range(n):
    numbers.remove(min(numbers))

for i in numbers:
    new_list.append(str(i))

print(", ".join(new_list))
