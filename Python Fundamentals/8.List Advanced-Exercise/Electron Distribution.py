number_of_electrons = int(input())

shells = []
number_of_shell = 0
sum_of_electrons = 0
while number_of_electrons > 0:
    number_of_shell += 1

    max_electrons = 2 * number_of_shell ** 2
    if max_electrons <= number_of_electrons:
        shells.append(max_electrons)
    else:
        shells.append(number_of_electrons)
    number_of_electrons -= max_electrons

print(shells)
