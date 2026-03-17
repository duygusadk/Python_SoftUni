num1 = int(input())

num2 = int(input())
sum = num1
num_list = []

for i in range(num2):
    num_list.append(sum)
    sum += num1

print(num_list)