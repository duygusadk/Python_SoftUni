command = input()

courses = {}
while ":" not in command:
    name, ID, course = command.split(":")

    courses[ID] = name, course


