word = ""
new_word = ""
while True:
    word = input()
    if word == "End":
        break
    elif word == "SoftUni":
        continue
    for i in word:
        new_word += i + i
    print(new_word)
    new_word = ""
