text = input()
command = input()

while command != "Decode":
    action = command.split("|")
    operation = action[0]

    if operation == "Move":
        n = int(action[1])
        text = text[n:] + text[:n]

    elif operation == "Insert":
        index = int(action[1])
        value = action[2]
        if 0 <= index <= len(text):
            text = text[:index] + value + text[index:]

    elif operation == "ChangeAll":
        substring = action[1]
        replacement = action[2]
        text=text.replace(substring,replacement)
    command = input()

print(f"The decrypted message is: {text}")