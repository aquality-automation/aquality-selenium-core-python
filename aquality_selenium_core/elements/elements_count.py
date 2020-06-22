"""Module defines enumeration for element counts."""
from enum import Enum


class ElementsCount(Enum):
    """Enumeration with possible count of elements."""

    ZERO = 0
    MORE_THEN_ZERO = 1
    ANY = 2
