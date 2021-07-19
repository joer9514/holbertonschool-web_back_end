#!/usr/bin/env python3
"""The function iterable tuple sequences"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function iterable sequence"""
    return [(i, len(i)) for i in lst]
