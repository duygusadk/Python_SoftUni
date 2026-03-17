string_nums = input().split(", ")

positive_list = [i for i in string_nums if int(i) >= 0]
negative_list = [i for i in string_nums if int(i) < 0]
even_list = [i for i in string_nums if int(i) % 2 == 0]
odd_list = [i for i in string_nums if int(i) % 2 != 0]

print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
