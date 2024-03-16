#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Complex types - functions with callable"""

    def multiplier_func(num: float) -> float:
        """ Inner function for the multiplication"""
        return num * multiplier
    return multiplier_func
