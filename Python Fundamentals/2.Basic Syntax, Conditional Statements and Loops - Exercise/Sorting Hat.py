word = ""

while True:

    word = input()

    if word == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif word == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(word) < 5:
        print(f"{word} goes to Gryffindor.")
    elif len(word) == 5:
        print(f"{word} goes to Slytherin.")
    elif len(word) == 6:
        print(f"{word} goes to Ravenclaw.")
    elif len(word) > 6:
        print(f"{word} goes to Hufflepuff.")
