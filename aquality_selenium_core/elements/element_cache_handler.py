"""Module defines abstraction for cached element handler."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.element_finder import AbstractElementFinder
from aquality_selenium_core.elements.element_state import ElementState


class AbstractElementCacheHandler(ABC):
    """Allows to use cached element."""

    @property
    @abstractmethod
    def is_stale(self) -> bool:
        """Determine whether the element stale or not."""
        pass

    @abstractmethod
    def is_refresh_needed(
        self, custom_state: ElementState = ElementState.DEFAULT
    ) -> bool:
        """
        Determine is the cached element refresh needed.

        :param custom_state: Custom element's existence state used for search.
        :return: true if needed and false otherwise.
        """
        pass

    @abstractmethod
    def get_element(
        self,
        timeout: timedelta = timedelta.min,
        custom_state: ElementState = ElementState.DEFAULT,
    ) -> WebElement:
        """
        Allow to get cached element.

        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Custom element's existence state used for search.
        :return: Cached element.
        """
        pass


class ElementCacheHandler(AbstractElementCacheHandler):
    """Allows to use cached element."""

    def __init__(self, locator: By, state: ElementState, finder: AbstractElementFinder):
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
        self, custom_state: ElementState = ElementState.DEFAULT
    ) -> bool:
        """
        Determine is the cached element refresh needed.

        :param custom_state: Custom element's existence state used for search.
        :return: true if needed and false otherwise.
        """
        if self.__remote_element is None:
            return True

        is_displayed = self.__remote_element.is_displayed()
        state = self.__resolve_state(custom_state)
        return state == ElementState.DISPLAYED and not is_displayed

    def get_element(
        self,
        timeout: timedelta = timedelta.min,
        custom_state: ElementState = ElementState.DEFAULT,
    ) -> WebElement:
        """
        Allow to get cached element.

        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Custom element's existence state used for search.
        :return: Cached element.
        """
        if self.is_refresh_needed(custom_state):
            state = self.__resolve_state(custom_state)
            self.__remote_element = self.__element_finder.find_element(
                self.__locator, state=state, timeout=timeout
            )
        return self.__remote_element

    def __resolve_state(self, custom_state: ElementState) -> ElementState:
        return self.__state if custom_state == ElementState.DEFAULT else custom_state
