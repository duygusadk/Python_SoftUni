text = input()

sorted_text = [i for i in text if i.lower() not in ['a', 'i', 'o', "u", "e"]]

print("".join(sorted_text))