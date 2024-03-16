#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> float:
    """ Complex types - string and int/float to tuple"""
    result: float = (k, v * v)
    return result
