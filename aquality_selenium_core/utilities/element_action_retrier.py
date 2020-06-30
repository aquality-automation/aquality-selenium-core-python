"""Module defines abstraction for retry functionality."""
from abc import ABC
from typing import TypeVar

TReturn = TypeVar("TReturn")


class AbstractElementActionRetrier(ABC):
    """Retries an action or function when defined exception occurs."""

    pass
