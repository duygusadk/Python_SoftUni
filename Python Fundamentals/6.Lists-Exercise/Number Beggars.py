strings = input()
beggars_count = int(input())

input_list = strings.split(", ")
sum_list = []
sum = 0
for i in range(beggars_count):
    for j in range(i, len(input_list), beggars_count):
        sum += int(input_list[j])

    sum_list.append(sum)
    sum = 0

print(sum_list)
