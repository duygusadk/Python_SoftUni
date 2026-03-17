n = int(input())

for i in range(n):
    word = input()

    if word.__contains__(".") or word.__contains__("_") or word.__contains__(","):
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
