"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List
import string

class OurAwesomeException(Exception):
    pass




def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    return id(first) == id(second)


def multiple_ints(first_value: int, second_value: int) -> int:
    if type(first_value) == int and type(second_value) == int:
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        return int(first_value) * int(second_value)
    except ValueError:
        return print("Not valid input data")


def is_word_in_text(word: str, text: str) -> bool:
    return word in text

def some_loop_exercise() -> list:
    listNew = []
    for i in range(0, 13):
        if i != 6 and i != 7:
            listNew.append(i)
    return listNew


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    listNew = []
    for i in data:
        if i > 0:
            listNew.append(i)
    return listNew


def alphabet() -> dict:
    letters = string.ascii_lowercase
    dictionary = {}
    for i in range(1, len(letters) + 1):
        dictionary[i] = letters[i-1]
    return dictionary

def simple_sort(data: List[int]) -> List[list]:
    for i in range(len(data) -1):
        for j in range(len(data) - 1 -i):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
