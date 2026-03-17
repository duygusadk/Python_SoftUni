n = int(input())
numbers = []
even_list = []
odd_list = []
positive_list = []
negative_list = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()
if command == "even":
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)

elif command == "odd":
    for i in numbers:
        if i % 2 != 0:
            odd_list.append(i)
    print(odd_list)
elif command == "negative":
    for i in numbers:
        if i < 0:
            negative_list.append(i)
    print(negative_list)
elif command == "positive":
    for i in numbers:
        if i >= 0:
            positive_list.append(i)
    print(positive_list)






