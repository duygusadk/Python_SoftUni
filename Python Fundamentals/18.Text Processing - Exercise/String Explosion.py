text = input()
final_string = ""
strength = 0
for i in range(len(text)):
    if strength > 0 and text[i] != ">":
        strength -= 1

    elif text[i] == ">":
        final_string += ">"
        strength += int(text[i + 1])
    else:
        final_string += text[i]


print(final_string)