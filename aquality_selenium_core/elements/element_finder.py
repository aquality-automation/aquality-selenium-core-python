"""Module defines abstraction for element finder."""
from abc import ABC
from datetime import timedelta
from typing import Callable
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AbstractElementFinder(ABC):
    """
    Provides ability to find elements by locator and search criteria.

    The criteria for search could be:
    - empty - to get all elements;
    - desired - from ElementState;
    - with - DesiredState;
    - with - Predicate.
    """

    def find_element(
        self,
        locator: By,
        element_state_condition: Callable[[WebElement], bool] = lambda element: True,
        timeout: timedelta = timedelta.min,
    ) -> WebElement:
        """
        Find element in desired ElementState or state defined by predicate.

        :param locator: element locator.
        :param element_state_condition: predicate to define element state.
        :param timeout: timeout for search.
        :return: Found element.
        :raises: NoSuchElementException if element was not found in time in desired state.
        """
        pass

    def find_elements(
        self,
        locator: By,
        element_state_condition: Callable[[WebElement], bool] = lambda element: True,
        timeout: timedelta = timedelta.min,
    ) -> List[WebElement]:
        """
        Find elements in desired ElementState or state defined by predicate.

        :param locator: element locator.
        :param element_state_condition: predicate to define element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass
