def change_symbol(s: str) -> str:
    return s.replace('#', '/')


def add_ing(s: str) -> str:
    return f"{s}ing"


def change_order(s: str) -> str:
    return " ".join(s.split()[::-1])


def clean_string(s: str) -> str:
    return s.strip()


def to_capitalize(s: str) -> str:
    return s.lower().capitalize()


def to_list(s: str) -> list:
    return s.split()


def formatting(array: list, s1: str, s2: str) -> str:
    return f"Hello, {array[0]} {array[1]}! {s1} to {s2}"


def to_string(array: list) -> str:
    return " ".join(array)


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array


def delete_from_list(array: list, indx: int) -> list:
    del array[indx]
    return array
