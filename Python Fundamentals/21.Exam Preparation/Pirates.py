command = input()
cities = {}
while command != "Sail":
    city, population, gold = command.split("||")

    if city not in cities:
        cities[city] = [int(population), int(gold)]
    else:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)
    command = input()

command = input()
while command != "End":
    action = command.split("=>")

    if action[0] == "Plunder":
        town = action[1]
        people = int(action[2])
        gold = int(action[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        cities[town][0] -= people
        cities[town][1] -= gold

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    elif action[0] == "Prosper":
        town = action[1]
        gold = int(action[2])

        if gold > 0:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    command = input()

if len(cities.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    for city, value in cities.items():
        print(f"{city} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
