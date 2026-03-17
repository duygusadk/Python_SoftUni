input_operator = input()
first_num = int(input())
second_num = int(input())


def calculate(input_operator, first_num, second_num):
    if input_operator == 'add':
        return first_num + second_num
    elif input_operator == 'subtract':
        return first_num - second_num
    elif input_operator == 'multiply':
        return first_num * second_num
    elif input_operator == 'divide' and second_num != 0:
        return first_num // second_num


print(calculate(input_operator, first_num, second_num))
