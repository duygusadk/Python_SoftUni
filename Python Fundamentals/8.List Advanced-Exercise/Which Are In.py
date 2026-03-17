first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_list = []

for i in first_sequence:
    for j in second_sequence:
        if i in j:
            new_list.append(i)
            break

print(new_list)
