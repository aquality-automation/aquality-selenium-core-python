"""Module defines abstraction for retry functionality."""
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Type

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException

from aquality_selenium_core.configurations.retry_configuration import (
    AbstractRetryConfiguration,
)
from aquality_selenium_core.utilities.action_retrier import AbstractActionRetrier
from aquality_selenium_core.utilities.action_retrier import ActionRetrier
from aquality_selenium_core.utilities.action_retrier import TReturn


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):
    """Abstract class for action retrier with elements."""

    @property
    @abstractmethod
    def get_handled_exceptions(self) -> List[Type[Exception]]:
        """
        Return supported exceptions.

        :return: Supported exceptions.
        """
        pass


class ElementActionRetrier(ActionRetrier, AbstractElementActionRetrier):
    """Retrier for action on elements."""

    def __init__(self, retry_configuration: AbstractRetryConfiguration):
        """Initialize retrier with configuration."""
        ActionRetrier.__init__(self, retry_configuration)

    def do_with_retry(
        self,
        function: Callable[..., TReturn],
        handled_exceptions: List[Type[Exception]] = [],
    ) -> TReturn:
        """
        Retry the action when the handled exception occurred.

        :param function: Action to be applied.
        :param handled_exceptions: Exceptions to be handled.
        :return: Result of the function.
        """
        exceptions_to_handle = (
            handled_exceptions if handled_exceptions else self.get_handled_exceptions()
        )
        return super().do_with_retry(function, exceptions_to_handle)

    def get_handled_exceptions(self) -> List[Type[Exception]]:
        """
        Return supported exceptions.

        :return: Supported exceptions.
        """
        return [StaleElementReferenceException, InvalidElementStateException]
