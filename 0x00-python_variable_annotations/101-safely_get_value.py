#!/usr/bin/env python3
""" Safely get the value and duck type"""
from typing import Union, TypeVar, Any, Mapping


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
