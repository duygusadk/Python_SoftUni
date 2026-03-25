text = input()
emoji = ""
emojies=[]
for i in range(len(text)):
    if text[i] == ":":
        emoji = text[i] + text[i + 1]
        emojies.append(emoji)


print("\n".join(emojies))