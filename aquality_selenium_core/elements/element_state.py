"""Module defines enumeration for element states."""
from enum import Enum


class ElementState(Enum):
    """Enumeration with possible element states."""

    DISPLAYED = "displayed"
    EXISTS_IN_ANY_STATE = "exists"
