#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """ Complex types - string and int/float to tuple"""
    result: Tuple[int, float] = (k, v * v)
    return result
