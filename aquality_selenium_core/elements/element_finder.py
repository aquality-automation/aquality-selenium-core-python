"""Module defines abstraction for element finder."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable
from typing import List
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.desired_state import DesiredState
from aquality_selenium_core.elements.element_state import ExistsInAnyState


class AbstractElementFinder(ABC):
    """Provides ability to find elements by locator and search criteria."""

    @abstractmethod
    def find_element(
        self,
        locator: Tuple[By, str],
        desired_state: Callable[[WebElement], bool] = ExistsInAnyState(),
        timeout: timedelta = timedelta.min,
    ) -> WebElement:
        """
        Find element in desired state defined by callable object.

        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: Found element.
        :raises: NoSuchElementException if element was not found in time in desired state.
        """
        pass

    @abstractmethod
    def find_elements(
        self,
        locator: Tuple[By, str],
        desired_state: Callable[[WebElement], bool] = ExistsInAnyState(),
        timeout: timedelta = timedelta.min,
    ) -> List[WebElement]:
        """
        Find elements in desired state defined by callable object.

        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass

    @abstractmethod
    def find_elements_in_state(
        self,
        locator: Tuple[By, str],
        desired_state: DesiredState,
        timeout: timedelta = timedelta.min,
    ):
        """
        Find elements in desired state defined by DesiredState object.

        :param locator: element locator.
        :param desired_state: desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass
