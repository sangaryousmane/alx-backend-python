#!/usr/bin/env python3
""" Sum complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """ Sum complex types - list of floats"""
    sum_ = 0.0
    
    for i in input_list:
        sum_ += i
    return sum_
