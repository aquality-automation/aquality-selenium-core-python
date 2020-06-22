"""Module defines abstraction for element state."""
from abc import ABC


class AbstractElementStateProvider(ABC):
    """
    Provides ability to define of element's state (whether it is displayed, exist or not).

    Also provides respective positive and negative waiting functions.
    """

    pass
