password = input()


def validate(password: str):
    is_valid = True
    digits = 0

    if len(password) > 10 or len(password) < 6:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    for i in password:
        if i.isdigit():
            digits += 1
    if digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


validate(password)
