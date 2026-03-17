number = int(input())


def perfect_num(num):
    sum = 0
    divisor = 1
    while sum < number:

        if num % divisor == 0:
            sum += divisor
        divisor += 1

    if sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_num(number)
