start = input()
end = input()


def all_characters(start, end) -> list:
    characters = []
    for i in range(ord(start) + 1, ord(end)):
        characters.append(chr(i))
    return characters


print(" ".join(all_characters(start, end)))
