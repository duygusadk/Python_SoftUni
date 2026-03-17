secret_message = input().split(" ")
digits = []
new_word = []
message = []
for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
        else:
            break

    first_letter = chr(int(number))
    rest = word[len(number):]
    rest = list(rest)
    rest[0], rest[-1] = rest[-1], rest[0]
    rest = "".join(rest)

    new_word = first_letter + rest
    message.append(new_word)

print(" ".join(message))
