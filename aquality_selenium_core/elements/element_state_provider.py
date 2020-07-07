"""Module defines abstraction for element state."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.desired_state import DesiredState
from aquality_selenium_core.elements.element_finder import AbstractElementFinder
from aquality_selenium_core.elements.element_state import Displayed
from aquality_selenium_core.elements.element_state import ExistsInAnyState
from aquality_selenium_core.waitings.conditional_wait import AbstractConditionalWait


class AbstractElementStateProvider(ABC):
    """
    Provides ability to define of element's state (whether it is displayed, exist or not).

    Also provides respective positive and negative waiting functions.
    """

    @property
    @abstractmethod
    def is_displayed(self) -> bool:
        """
        Get element's displayed state.

        :return: true if displayed and false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_exist(self) -> bool:
        """
        Get element's exist state.

        :return: true if element exists in DOM (without visibility check) and false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        """
        Get element's Enabled state, which means element is Enabled and does not have "disabled" class.

        :return: true if enabled, false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_clickable(self) -> bool:
        """
        Get element's clickable state, which means element is displayed and enabled.

        :return: true if element is clickable, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_displayed(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element is displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_displayed(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element is not displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element is not displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_exist(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element exists in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_exist(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element does not exist in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element does not exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_enabled(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element has enabled state which means element is Enabled and does not have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_not_enabled(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element does not have enabled state which means element is not Enabled or does have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if not enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_clickable(self, timeout: timedelta = timedelta.min) -> None:
        """
        Wait for element to become clickable which means element is displayed and enabled.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :raises: WebDriverTimeoutException when timeout exceeded and element is not clickable.
        """
        pass


class ElementStateProvider(AbstractElementStateProvider):
    """
    Provides ability to define of element's state (whether it is displayed, exist or not).

    Also provides respective positive and negative waiting functions.
    """

    def __init__(
        self,
        element_locator: By,
        conditional_wait: AbstractConditionalWait,
        element_finder: AbstractElementFinder,
    ):
        """Initialize provider with required dependencies."""
        self.__element_locator = element_locator
        self.__conditional_wait = conditional_wait
        self.__element_finder = element_finder

    @property
    def is_displayed(self) -> bool:
        """
        Get element's displayed state.

        :return: true if displayed and false otherwise.
        """
        return self.wait_for_displayed(timedelta())

    @property
    def is_exist(self) -> bool:
        """
        Get element's exist state.

        :return: true if element exists in DOM (without visibility check) and false otherwise.
        """
        return self.wait_for_exist(timedelta())

    @property
    def is_enabled(self) -> bool:
        """
        Get element's Enabled state, which means element is Enabled and does not have "disabled" class.

        :return: true if enabled, false otherwise.
        """
        return self.wait_for_enabled(timedelta())

    @property
    def is_clickable(self) -> bool:
        """
        Get element's clickable state, which means element is displayed and enabled.

        :return: true if element is clickable, false otherwise.
        """
        return self.__is_element_clickable(timedelta(), True)

    def wait_for_displayed(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element is displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element displayed after waiting, false otherwise.
        """
        return self.__is_any_element_found(timeout, Displayed())

    def wait_for_not_displayed(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element is not displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element is not displayed after waiting, false otherwise.
        """
        return self.__conditional_wait.wait_for(lambda: not self.is_displayed, timeout)

    def wait_for_exist(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element exists in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element exist after waiting, false otherwise.
        """
        return self.__is_any_element_found(timeout, ExistsInAnyState())

    def wait_for_not_exist(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element does not exist in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element does not exist after waiting, false otherwise.
        """
        return self.__conditional_wait.wait_for(lambda: not self.is_exist, timeout)

    def wait_for_enabled(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element has enabled state which means element is Enabled and does not have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        return self.__is_element_in_desired_condition(
            timeout, lambda element: bool(element.is_enabled()), "ENABLED"
        )

    def wait_for_not_enabled(self, timeout: timedelta = timedelta.min) -> bool:
        """
        Wait for element does not have enabled state which means element is not Enabled or does have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if not enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        return self.__is_element_in_desired_condition(
            timeout, lambda element: not bool(element.is_enabled()), "NOT ENABLED"
        )

    def wait_for_clickable(self, timeout: timedelta = timedelta.min) -> None:
        """
        Wait for element to become clickable which means element is displayed and enabled.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :raises: WebDriverTimeoutException when timeout exceeded and element is not clickable.
        """
        self.__is_element_clickable(timeout, False)

    def __is_any_element_found(self, timeout: timedelta, state: Callable) -> bool:
        found_elements = self.__element_finder.find_elements(
            self.__element_locator, state, timeout
        )
        return len(found_elements) > 0

    def __is_element_clickable(
        self, timeout: timedelta, catch_timeout_exception: bool
    ) -> bool:
        desired_state = DesiredState(
            lambda element: bool(element.is_displayed()) and bool(element.is_enabled()),
            "CLICKABLE",
            catch_timeout_exception,
        )
        return self.__is_element_in_desired_state(timeout, desired_state)

    def __is_element_in_desired_condition(
        self,
        timeout: timedelta,
        desired_condition: Callable[[WebElement], bool],
        state_name: str,
    ) -> bool:
        desired_state = DesiredState(desired_condition, state_name, True, True)
        return self.__is_element_in_desired_state(timeout, desired_state)

    def __is_element_in_desired_state(
        self, timeout: timedelta, desired_state: DesiredState
    ) -> bool:
        found_elements = self.__element_finder.find_elements_in_state(
            self.__element_locator, desired_state, timeout
        )
        return len(found_elements) > 0
