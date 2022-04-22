from typing import Dict, Union, Callable
from .function_set import *


def get_function_setting(function_number: int) -> Dict[int, Dict[str, Union[Callable, int, list]]]:
    if function_number < 1 or function_number > 7:
        raise("The parameter `function_number` should be in [1, 7]")

    return {
        1: {
            "function": function_1,
            "dimension": 30,
            "boundary": [-10, 10]
        },
        2: {
            "function": function_2,
            "dimension": 30,
            "boundary": [-100, 100]
        },
        3: {
            "function": function_3,
            "dimension": 30,
            "boundary": [-600, 600]
        },
        4: {
            "function": function_4,
            "dimension": 30,
            "boundary": [-50, 50]
        },
        5: {
            "function": function_5,
            "dimension": 30,
            "boundary": [-50, 50]
        },
        6: {
            "function": function_6,
            "dimension": 2,
            "boundary": [-65, 65]
        },
        7: {
            "function": function_7,
            "dimension": 4,
            "boundary": [-5, 5]
        }
    }[function_number]