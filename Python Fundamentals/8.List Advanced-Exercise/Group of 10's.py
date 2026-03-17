sequence_of_numbers = input().split(", ")
numbers = [int(i) for i in sequence_of_numbers]

min = 0
for group in range(10, max(numbers)+10, 10):
    new_list = [i for i in numbers if group >= i > min]
    print(f"Group of {group}'s: {new_list}")
    new_list.clear()
    min = group
