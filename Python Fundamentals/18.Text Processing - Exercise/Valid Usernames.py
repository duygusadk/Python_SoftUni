usernames = input().split(", ")


def len_is_valid(name) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False


def symbols_are_valid(name: str) -> bool:
    for ch in name:
        if not (ch.isalnum() or ch == '_' or ch == '-'):
            return False
    return True


def no_redundant_symbols(name) -> bool:
    if " " in name:
        return False
    return True


def username_is_valid(name) -> bool:
    if len_is_valid(name) and symbols_are_valid(name) and no_redundant_symbols(name):
        return True


for name in usernames:
    if username_is_valid(name):
        print(name)
