number_of_rooms = int(input())
sum = 0
is_free = True
for i in range(number_of_rooms):
    room = input().split(" ")

    if len(room[0]) < int(room[1]):
        needed_chairs_in_room = int(room[1]) - len(room[0])
        is_free = False
        print(f"{needed_chairs_in_room} more chairs needed in room {i+1}")
    else:
        total_free_chairs = len(room[0]) - int(room[1])
        sum += total_free_chairs

if is_free:
    print(f"Game On, {sum} free chairs left")
