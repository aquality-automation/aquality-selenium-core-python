# -*- coding: utf-8 -*-
from enum import Enum


class ElementsCount(Enum):
    """
    Possible count of elements.
    """

    ZERO = 0
    MORE_THEN_ZERO = 1
    ANY = 2
