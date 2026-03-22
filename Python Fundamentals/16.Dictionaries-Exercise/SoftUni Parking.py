n = int(input())

parking = {}
for i in range(n):
    command = input().split(" ")
    username = command[1]

    if command[0] == "register":

        license_plate_number = command[2]
        if username not in parking.keys():
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command[0] == "unregister":
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
