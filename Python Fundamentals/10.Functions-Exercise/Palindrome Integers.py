string_numbers = input().split(", ")
palindrome_numbers = []


def is_palindrome(num):
    for i in string_numbers:

        if "".join(reversed(i)) == i:
            print(True)
        else:
            print(False)


is_palindrome(string_numbers)
