coded_message = input()
command = input()

while command != "Finalize":

    operation = command.split(" ")

    if operation[0] == "Encrypt":
        coded_message = coded_message[::-1]
        print(coded_message)
    elif operation[0] == "Decrypt":
        coded_message = coded_message.swapcase()
        print(str(coded_message))
    elif operation[0] == "Substitute":
        old_char = operation[1]
        new_char = operation[2]

        if old_char in coded_message:
            coded_message = coded_message.replace(old_char, new_char)
            print(coded_message)
        else:
            print("Character not found.")
    elif operation[0] == "Scramble":
        index = int(operation[1])
        char = operation[2]

        if 0 <= index < len(coded_message):
            coded_message = coded_message[:index] + char + coded_message[index+1:]
            print(coded_message)
        else:
            print("Index out of bounds.")

    elif operation[0] == "Remove":
        substring = operation[1]
        coded_message = coded_message.replace(substring, "")
        print(coded_message)
    else:
        print("Invalid command detected!")
    command = input()
