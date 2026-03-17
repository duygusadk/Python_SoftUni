to_do_notes = [0] * 10
command = ""
while True:
    command = input()
    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0]) - 1

    to_do_notes.pop(priority)
    to_do_notes.insert(priority, tokens[1])

notes = [note for note in to_do_notes if note != 0]
print(notes)
