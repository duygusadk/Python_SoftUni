num1 = int(input())
num2 = int(input())
num3 = int(input())


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    final_result=subtract(result,num3)

    return final_result


def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum, num3):
    return sum - num3


print(add_and_subtract(num1, num2, num3))
