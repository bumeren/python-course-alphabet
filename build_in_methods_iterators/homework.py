from typing import List, Dict, Union, Generator
import random
import string
# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
   for elem in data:
        for k, v in elem.items():
            if k == 'name':
               elem[k] = v.capitalize()
   return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    for elem in data:
        for element in redundant_keys:
            del elem[element]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    for elem in data:
        for keys, values in elem.items():
            if values == value:
                return elem


def task_4_min_value_integers(data: List[int]) -> int:
    return min([int(elem) for elem in data])

def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    return min(data, key=lambda x: len(x))


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    max_list = []
    for elem in data:
        for keys, values in elem.items():
            if keys == key:
                max_list.append(values)
    return max(max_list)

def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    return max([int(elements) for elem in data for elements in elem])


def task_8_sum_of_ints(data: List[int]) -> int:
    return sum(elem for elem in data)


def task_9_sum_characters_positions(text: str) -> int:
    return sum(ord(elem) for elem in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    return (elem for elem in range(200))


def task_11_create_list_of_random_characters() -> List[str]:
    return [random.choice(string.ascii_letters) for _ in range(20)]
