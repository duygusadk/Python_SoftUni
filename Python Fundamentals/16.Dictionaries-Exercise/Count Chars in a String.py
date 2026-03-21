text = input()

characters = {}
for i in text:
    if i != " ":
        if i not in characters.keys():
            characters[i] = 1
        else:
            characters[i] += 1

for key, value in characters.items():
    print(f"{key} -> {value}")
