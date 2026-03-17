initial_list = input().split("!")
command = " "


def urgent_item(items: list, item):
    if item not in items:
        items.insert(0,item)


def unnecessary_item(items: list, item):
    if item in items:
        items.remove(item)


def correct_item(items: list, old_item, new_item):
    if old_item in items:
        old_item_position = items.index(old_item)
        items.remove(old_item)
        items.insert(old_item_position, new_item)


def rearrange_item(items: list, item):
    if item in items:
        items.remove(item)
        items.append(item)


while command != "Go Shopping!":
    command = input().split(" ")
    if command[0] == "Urgent":
        urgent_item(initial_list, command[1])
    elif command[0] == "Unnecessary":
        unnecessary_item(initial_list, command[1])
    elif command[0] == "Correct":
        correct_item(initial_list, command[1], command[2])
    elif command[0] == "Rearrange":
        rearrange_item(initial_list, command[1])
    command = " ".join(command)
print(", ".join(initial_list))
