"""Module defines abstraction for cached element handler."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable
from typing import cast
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.element_finder import AbstractElementFinder
from aquality_selenium_core.elements.element_state import Displayed


class AbstractElementCacheHandler(ABC):
    """Allows to use cached element."""

    @property
    @abstractmethod
    def is_stale(self) -> bool:
        """Determine is the element stale."""
        pass

    @abstractmethod
    def is_refresh_needed(
        self, custom_state: Callable[[WebElement], bool] = cast(Callable, None)
    ) -> bool:
        """
        Determine is the cached element refresh needed.

        :param custom_state: Element custom state.
        :return: true if needed and false otherwise.
        """
        pass

    @abstractmethod
    def get_element(
        self,
        timeout: timedelta = timedelta.min,
        custom_state: Callable[[WebElement], bool] = cast(Callable, None),
    ) -> WebElement:
        """
        Allow to get cached element.

        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Element custom state.
        :return: Cached element.
        """
        pass


class ElementCacheHandler(AbstractElementCacheHandler):
    """Allows to use cached element."""

    def __init__(
        self, locator: Tuple[By, str], state: Callable, finder: AbstractElementFinder
    ):
        """Initialize handler with default state and finder."""
        self.__locator = locator
        self.__state = state
        self.__element_finder = finder
        self.__remote_element = None

    @property
    def is_stale(self) -> bool:
        """Determine whether the element stale or not."""
        return self.__remote_element is not None and self.is_refresh_needed()

    def is_refresh_needed(
        self, custom_state: Callable[[WebElement], bool] = cast(Callable, None)
    ) -> bool:
        """
        Determine is the cached element refresh needed.

        :param custom_state: Element custom state.
        :return: true if needed and false otherwise.
        """
        if self.__remote_element is None:
            return True

        state = self.__state if custom_state is None else custom_state
        is_displayed = self.__remote_element.is_displayed()
        return isinstance(state, Displayed) and not is_displayed

    def get_element(
        self,
        timeout: timedelta = timedelta.min,
        custom_state: Callable[[WebElement], bool] = cast(Callable, None),
    ) -> WebElement:
        """
        Allow to get cached element.

        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Element custom state.
        :return: Cached element.
        """
        if self.is_refresh_needed(custom_state):
            self.__remote_element = self.__element_finder.find_element(
                self.__locator, self.__state, timeout
            )
        return self.__remote_element
