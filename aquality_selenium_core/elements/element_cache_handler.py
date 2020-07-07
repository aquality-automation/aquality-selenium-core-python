"""Module defines abstraction for cached element handler."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable

from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.element_state import ExistsInAnyState


class AbstractElementCacheHandler(ABC):
    """Allows to use cached element."""

    @property
    @abstractmethod
    def is_stale(self) -> bool:
        """Determine is the element stale."""
        pass

    @abstractmethod
    def is_refresh_needed(self, custom_state: Callable = ExistsInAnyState()) -> bool:
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
        custom_state: Callable = ExistsInAnyState(),
    ) -> WebElement:
        """
        Allow to get cached element.

        :param timeout: Timeout used to retrieve the element when refresh is needed.
        :param custom_state: Custom element's existence state used for search.
        :return: Cached element.
        """
        pass
