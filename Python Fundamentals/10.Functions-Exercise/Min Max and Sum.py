string_numbers = input().split()
numbers = []

for i in string_numbers:
    numbers.append(int(i))

minimum_number=min(numbers)
maximum_number=max(numbers)
sum_of_all_numbers=sum(numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")