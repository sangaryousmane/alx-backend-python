#!/usr/bin/env python3
"""  Complex types - mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Complex types - mixed list"""
    sum_: float = 0.0

    for i in mxd_lst:
        sum_ += i
    return sum_
