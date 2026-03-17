command = ""
coffees = 0
while True:

    command = input()

    if command == "END":
        break
    if command == "dog" or command == "cat" or command == "movie" or command == "coding":
        coffees += 1
    elif command == "DOG" or command == "CAT" or command == "MOVIE" or command == "CODING":
        coffees += 2
if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")
