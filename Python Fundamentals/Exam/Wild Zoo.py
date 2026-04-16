command = input()
zoo = {}
areas = {}
while command != "EndDay":
    action = command.split(": ")

    if action[0] == "Add":
        animal_name, needed_food, area = action[1].split("-")
        needed_food_quantity = int(needed_food)

        if animal_name not in zoo.keys():
            zoo[animal_name] = {"needed_food_quantity": needed_food_quantity, "area": area}
            if area not in areas:
                areas[area] = 1
            else:
                areas[area] += 1
        else:
            zoo[animal_name]["needed_food_quantity"] += needed_food_quantity
            zoo[animal_name]["area"] = area
    elif action[0] == "Feed":
        animalName, food = action[1].split("-")
        food_quantity = int(food)

        if animalName in zoo.keys():
            zoo[animalName]["needed_food_quantity"] -= food_quantity
            if zoo[animalName]["needed_food_quantity"] <= 0:
                area = zoo[animalName]["area"]
                print(f"{animalName} was successfully fed")
                del zoo[animalName]
                areas[area] -= 1
    command = input()

print("Animals:")
for animal, value in zoo.items():
    print(f" {animal} -> {value['needed_food_quantity']}g")

print("Areas with hungry animals:")
for area_name, count in areas.items():
    if count > 0:
        print(f" {area_name}: {count}")
