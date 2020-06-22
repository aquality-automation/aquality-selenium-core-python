"""Module defines abstraction for element finder."""
from abc import ABC


class AbstractElementFinder(ABC):
    """
    Provides ability to find elements by locator and search criteria.

    The criteria for search could be:
    - empty - to get all elements;
    - desired - from ElementState;
    - with - DesiredState;
    - with - Predicate.
    """

    pass
