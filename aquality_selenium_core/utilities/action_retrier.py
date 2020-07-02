"""Module defines work with repeated actions."""
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Type
from typing import TypeVar

TReturn = TypeVar("TReturn")


class AbstractActionRetrier(ABC):
    """Abstract class for action retrier."""

    @abstractmethod
    def do_with_retry(
        self,
        function: Callable[..., TReturn],
        handled_exceptions: List[Type[Exception]] = [],
    ) -> TReturn:
        """
        Try to execute function repeatedly.

        :param function: Function to retry.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass
