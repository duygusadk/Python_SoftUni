number = int(input())


def odd_even_sum(number):
    sum_even = 0
    sum_odd = 0

    while number > 0:

        last_digit = number % 10

        if last_digit % 2 == 0:
            sum_even += last_digit
        else:
            sum_odd += last_digit

        number = number // 10
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


print(odd_even_sum(number))