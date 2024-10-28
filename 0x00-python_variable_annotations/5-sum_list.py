#!/usr/bin/env python3
"""Write a type-annotated func sum_list that takes a list
Input_list of float as an argument and returns sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum as a float"""
    return float(sum(input_list))
