#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """ Complex types - string and int/float to tuple"""
    return (k, v * v)