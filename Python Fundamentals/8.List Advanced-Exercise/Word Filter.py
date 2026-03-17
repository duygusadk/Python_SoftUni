text = input().split(" ")

filtered_list = [i for i in text if len(i) % 2 == 0]

print("\n".join(filtered_list))
