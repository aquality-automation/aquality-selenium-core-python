"""Module defines waiting functionality."""
import time
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable
from typing import cast
from typing import List
from typing import Type
from typing import TypeVar

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from aquality_selenium_core.applications.application import AbstractApplication
from aquality_selenium_core.configurations.timeout_configuration import (
    AbstractTimeoutConfiguration,
)

T = TypeVar("T")


class AbstractConditionalWait(ABC):
    """Utility used to wait for some condition."""

    @abstractmethod
    def wait_for_with_driver(
        self,
        condition: Callable[[WebDriver], T],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        message: str = "",
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> T:
        """
        Wait for some condition using WebDriver within timeout.

        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of TimeoutException.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: Result of condition.
        :raises: TimeoutException when timeout exceeded and condition not satisfied.
        """
        pass

    @abstractmethod
    def wait_for(
        self,
        condition: Callable[..., bool],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> bool:
        """
        Wait for some condition within timeout.

        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: True if condition satisfied and false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_true(
        self,
        condition: Callable[..., bool],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        message: str = "",
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> None:
        """
        Wait for some condition within timeout.

        :param condition: Predicate for waiting.
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of Timeout exception.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        """
        pass


class ConditionalWait(AbstractConditionalWait):
    """This class is used for waiting any conditions."""

    def __init__(
        self,
        timeout_configuration: AbstractTimeoutConfiguration,
        application: AbstractApplication,
    ):
        """Initialize with configuration."""
        self.__timeout_configuration = timeout_configuration
        self.__application = application

    def wait_for_with_driver(
        self,
        condition: Callable[[WebDriver], T],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        message: str = "",
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> T:
        """
        Wait for some condition using WebDriver within timeout.

        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of TimeoutException.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: Result of condition.
        :raises: TimeoutException when timeout exceeded and condition not satisfied.
        """
        wait_timeout = self.__resolve_condition_timeout(timeout)
        check_interval = self.__resolve_polling_interval(polling_interval)
        ignored_exceptions = (
            exceptions_to_ignore
            if exceptions_to_ignore
            else [StaleElementReferenceException]
        )
        self.__application.set_implicit_wait_timeout(timedelta())
        wait = WebDriverWait(
            self.__application.driver, wait_timeout, check_interval, ignored_exceptions
        )
        try:
            return cast(T, wait.until(condition, message))
        finally:
            self.__application.set_implicit_wait_timeout(
                self.__timeout_configuration.implicit
            )

    def wait_for(
        self,
        condition: Callable[..., bool],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> bool:
        """
        Wait for some condition within timeout.

        :param condition: Function for waiting
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        :return: True if condition satisfied and false otherwise.
        """

        def func():
            self.wait_for_true(
                condition,
                timeout,
                polling_interval,
                exceptions_to_ignore=exceptions_to_ignore,
            )
            return True

        return self.__is_condition_satisfied(func, [TimeoutError])

    def wait_for_true(
        self,
        condition: Callable[..., bool],
        timeout: timedelta = cast(timedelta, None),
        polling_interval: timedelta = cast(timedelta, None),
        message: str = "",
        exceptions_to_ignore: List[Type[Exception]] = [],
    ) -> None:
        """
        Wait for some condition within timeout.

        :param condition: Predicate for waiting.
        :param timeout: Condition timeout (in seconds). Default value is taken from configuration.
        :param polling_interval: Condition check interval (in milliseconds). Default value is taken from configuration.
        :param message: Part of error message in case of Timeout exception.
        :param exceptions_to_ignore: Possible exceptions that have to be ignored.
        """
        wait_timeout = self.__resolve_condition_timeout(timeout)
        check_interval = self.__resolve_polling_interval(polling_interval)
        start_time = time.time()

        while True:
            if self.__is_condition_satisfied(condition, exceptions_to_ignore):
                return

            current_time = time.time()
            if (current_time - start_time) > wait_timeout:
                raise TimeoutError(
                    f"Timed out after {wait_timeout} seconds during wait for condition '{message}'"
                )

            time.sleep(check_interval)

    @staticmethod
    def __is_condition_satisfied(
        condition: Callable[..., bool], exceptions_to_ignore: List[Type[Exception]] = []
    ) -> bool:
        try:
            return condition()
        except Exception as exception:
            if any(
                isinstance(exception, ignored_exception)
                for ignored_exception in exceptions_to_ignore
            ):
                return False
            raise

    def __resolve_condition_timeout(self, timeout: timedelta) -> int:
        condition_timeout = (
            timeout if timeout is not None else self.__timeout_configuration.condition
        )
        return condition_timeout.seconds

    def __resolve_polling_interval(self, polling_interval: timedelta) -> int:
        interval = (
            polling_interval
            if polling_interval is not None
            else self.__timeout_configuration.polling_interval
        )
        return interval.seconds
