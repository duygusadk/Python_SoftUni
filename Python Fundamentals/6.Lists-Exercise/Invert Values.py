string = input()

num_list = string.split(" ")
new_list = []

for num in num_list:
    new_list.append(-int(num))
print(new_list)
