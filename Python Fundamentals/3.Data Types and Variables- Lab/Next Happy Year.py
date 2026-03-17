
year = int(input())
digits = 0
while True:
    year += 1
    year_str = str(year)

    num_set = set(year_str)

    if len(num_set) == len(year_str):
        print(year)
        break
