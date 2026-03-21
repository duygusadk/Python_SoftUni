phonebook = {}
num = 0
while True:
    info = input()
    if "-" in info:
        phone_number = info.split("-")

        phonebook[phone_number[0]] = phone_number[1]

    else:
        num = int(info)
        break

for i in range(0, num):
    name = input()

    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
