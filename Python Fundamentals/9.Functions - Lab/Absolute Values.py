list_of_strings = input().split()
absolute_number_list=[]
numbers=[]
for i in list_of_strings:
    numbers.append(float(i))

for i in numbers:
    absolute_number_list.append(abs(i))

print(absolute_number_list)