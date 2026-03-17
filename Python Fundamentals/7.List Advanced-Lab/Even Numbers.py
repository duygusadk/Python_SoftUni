string_number_list = input().split(", ")
number_list = []
index_list = []
for string in string_number_list:
    number_list.append(int(string))

for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        index_list.append(i)

print(index_list)
