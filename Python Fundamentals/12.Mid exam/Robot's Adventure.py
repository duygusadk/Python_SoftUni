integers = [int(integer) for integer in input().split("|")]

total_items_collected = 0
while True:
    command = input()

    if command == "Adventure over":
        break
    command = command.split("$")

    if command[0] == "Step Backward":
        start_index = int(command[1])
        steps = int(command[2])
        if 0 <= start_index < len(integers):
            new_index = start_index
            for i in range(steps):
                new_index -= 1
                if new_index < 0:
                    new_index = len(integers) - 1
            total_items_collected += integers[new_index]
            integers[new_index] = 0

    elif command[0] == "Step Forward":
        start_index = int(command[1])
        steps = int(command[2])
        if 0 <= start_index < len(integers):
            new_index = start_index
            for i in range(steps):
                new_index += 1
                if new_index == len(integers):
                    new_index = 0
            total_items_collected += integers[new_index]
            integers[new_index] = 0
    elif command[0].startswith("Double"):
        commands = command[0].split()
        index = int(commands[1])
        if 0 <= index < len(integers):
            integers[index] *= 2
    elif command[0] == "Switch":
        integers.reverse()

print(" - ".join(map(str, integers)))
print(f"Robo finished the adventure with {total_items_collected} items!")
