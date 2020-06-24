"""Module defines work with repeated actions."""
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Type
from typing import TypeVar

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException

T = TypeVar("T")


class AbstractActionRetrier(ABC):
    """Abstract class for action retrier."""

    @abstractmethod
    def do_with_retry(
        self,
        function: Callable[..., T],
        handled_exceptions: List[Type[Exception]] = [],
    ) -> T:
        """
        Try to execute function repeatedly.

        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):
    """Abstract class for action retrier with elements."""

    @abstractmethod
    def do_with_retry(
        self,
        function: Callable[..., T],
        handled_exceptions: List[Type[Exception]] = [],
    ) -> T:
        """
        Try to execute function related to element actions.

        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass

    @staticmethod
    def get_handled_exceptions() -> List[Type[Exception]]:
        """
        Return supported exceptions.

        :return: Supported exceptions.
        """
        return [StaleElementReferenceException, InvalidElementStateException]
