from exceptions import VersionError


def reformat(version: str):
    last_digit, last_letter, last_dot = False, False, False

    def insert_digit(digit: str):
        nonlocal last_dot, last_digit, last_letter
        if last_digit or last_dot:
            return digit
        elif last_letter:
            return f".{digit}"
        elif not last_digit and not last_dot and not last_letter:
            return digit

    def insert_letter(letter: str):
        nonlocal last_dot, last_digit, last_letter
        if last_letter or last_dot:
            return letter
        elif last_digit:
            return f".{letter}"

    version_old = version.replace("_", ".").replace("-", ".").replace("+", ".").replace("/", ".").replace("\\", ".")
    version_new = ""

    for symbol in version_old:
        if symbol.isdigit():
            version_new += insert_digit(symbol)
            last_letter, last_dot = False, False
            last_digit = True
        elif symbol.isalpha():
            version_new += insert_letter(symbol)
            last_digit, last_dot = False, False
            last_letter = True
        elif symbol == "." or symbol == "#":
            version_new += symbol
            last_letter, last_digit = False, False
            last_dot = True

    return version_new


def to_list(version: str):
    if version is None:
        raise VersionError("Version arg must be a str object")
    version = reformat(version)
    version_list = version.split(".")
    return version_list


def equalize_lengths(lst_1: list, lst_2: list):
    if len(lst_1) != len(lst_2):
        difference = abs(len(lst_1) - len(lst_2))
        less = min(lst_1, lst_2, key=lambda a: len(a))
        less.extend(["_" for _ in range(difference)])
    return lst_1, lst_2
