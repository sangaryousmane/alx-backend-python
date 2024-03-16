#!/usr/bin/env python3
""" Let's duck type an iterable object"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Let's duck type an iterable object"""

    if lst:
        return lst[0]
    else:
        return None
