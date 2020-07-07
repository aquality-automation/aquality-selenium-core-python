"""Module defines work with repeated actions."""
import time
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import cast
from typing import List
from typing import Type
from typing import TypeVar

from aquality_selenium_core.configurations.retry_configuration import (
    AbstractRetryConfiguration,
)

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


class ActionRetrier(AbstractActionRetrier):
    """Action retrier."""

    def __init__(self, retry_configuration: AbstractRetryConfiguration):
        """Initialize retrier with configuration."""
        self.__retry_configuration = retry_configuration

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
        retry_attempts_left = self.__retry_configuration.number
        result = cast(TReturn, None)

        while retry_attempts_left >= 0:
            try:
                result = function()
                break
            except Exception as exception:
                if (
                    self.__is_exception_handled(exception, handled_exceptions)
                    and retry_attempts_left != 0
                ):
                    time.sleep(self.__retry_configuration.polling_interval.seconds)
                    retry_attempts_left -= 1
                else:
                    raise
        return result

    @staticmethod
    def __is_exception_handled(
        exception: Exception, handled_exceptions: List[Type[Exception]]
    ) -> bool:
        return any(
            isinstance(exception, handled_exception)
            for handled_exception in handled_exceptions
        )
