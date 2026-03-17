desk_of_cards = input().split()
number_of_shuffles = int(input())

for current_shuffle in range(number_of_shuffles):
    middle_of_desk = len(desk_of_cards) // 2
    first_part = desk_of_cards[:middle_of_desk]
    second_part = desk_of_cards[middle_of_desk:]
    new_list = []
    for card_index in range(len(first_part)):
        new_list.append(first_part[card_index])
        new_list.append(second_part[card_index])
    desk_of_cards = new_list.copy()
print(new_list)
