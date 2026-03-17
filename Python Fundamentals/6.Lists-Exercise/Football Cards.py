cards = input()

cards_list = cards.split(" ")
team_A = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
team_B = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
new_list = []
is_terminated = False
for i in cards_list:
    new_list.append(i.split("-"))

for i in new_list:

    if i[0] == "A":
        if team_A.__contains__(i[1]):
            team_A.remove(i[1])
    else:
        if team_B.__contains__(i[1]):
            team_B.remove(i[1])

    if len(team_A) <= 6 or len(team_B) <= 6:
        is_terminated = True
        break

if is_terminated:
    print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
