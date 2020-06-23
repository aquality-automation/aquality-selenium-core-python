"""Module defines work with repeated actions."""
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Type

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException


class AbstractActionRetrier(ABC):
    """Abstract class for action retrier."""

    @abstractmethod
    def do_with_retry(
        self,
        function_and_args: List[Type[Any]],
        handled_exceptions: List[Type[Exception]],
    ) -> Any:
        """
        Try to execute function repeatedly.

        :param function_and_args: Function to retry with arguments.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):
    """Abstract class for action retrier with elements."""

    @abstractmethod
    def do_with_retry(
        self,
        function_and_args: List[Type[Any]],
        handled_exceptions: List[Type[Exception]],
    ) -> Any:
        """
        Try to execute function related to element actions.

        :param function_and_args: Function to retry with arguments.
        :param handled_exceptions: Exceptions which will be catches during function execution.
        :return: Result of executed function.
        """
        pass

    def get_handled_exceptions(self) -> List[Type[Exception]]:
        """
        Return supported exceptions.

        :return: Supported exceptions.
        """
        return [StaleElementReferenceException, InvalidElementStateException]
