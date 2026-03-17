initial_energy = float(input())
command = input()
legendary_artifact = 0
visited_mountain = 0
failed = False
while command != "Journey ends here!":

    if command == "mountain":
        initial_energy -= 10
        visited_mountain += 1
        if visited_mountain % 3 == 0:
            legendary_artifact += 1

    elif command == "desert":
        initial_energy -= 15
    elif command == "forest":
        initial_energy += 7

    if legendary_artifact == 3:
        print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
        break
    if initial_energy <= 0:
        failed = True
        print("The character is too exhausted to carry on with the journey.")
        break

    command = input()

if not failed:
    if legendary_artifact < 3:
        print(
            f"The character could not find all the pieces and needs {3 - legendary_artifact} more to complete the legendary artifact.")
