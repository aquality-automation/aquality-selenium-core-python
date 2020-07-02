"""Module defines abstraction for retry functionality."""
from abc import ABC
from typing import List
from typing import Type

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException

from aquality_selenium_core.utilities.action_retrier import AbstractActionRetrier


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):
    """Abstract class for action retrier with elements."""

    @staticmethod
    def get_handled_exceptions() -> List[Type[Exception]]:
        """
        Return supported exceptions.

        :return: Supported exceptions.
        """
        return [StaleElementReferenceException, InvalidElementStateException]
