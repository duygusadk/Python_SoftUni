string_numbers = input().split()
numbers = []


def is_even(number: int) -> bool:
    return number % 2 == 0


for i in string_numbers:
    numbers.append(int(i))

even_numbers = list(filter(is_even, numbers))

print(even_numbers)
