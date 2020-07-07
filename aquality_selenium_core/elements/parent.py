"""Module defines abstraction for element with child elements."""
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Tuple
from typing import TypeVar

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.element_state import Displayed
from aquality_selenium_core.elements.elements_count import ElementsCount

TElement = TypeVar("TElement")


class AbstractParent(ABC):
    """Defines behavior of element with child elements."""

    @abstractmethod
    def find_child_element(
        self,
        child_locator: Tuple[By, str],
        name: str,
        supplier: Callable[[Tuple[By, str], str, Callable], TElement],
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> TElement:
        """
        Find child element ot type TElement of current element by its locator.

        :param child_locator: Locator of child element.
        :param name: Child element name.
        :param supplier: Delegate that defines constructor of child element in case of custom element.
        :param state: Child element state.
        :return: Instance of child element.
        """
        pass

    @abstractmethod
    def find_child_elements(
        self,
        child_locator: Tuple[By, str],
        name: str,
        supplier: Callable[[Tuple[By, str], str, Callable], TElement],
        expected_count: ElementsCount = ElementsCount.ANY,
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> List[TElement]:
        """
        Find child elements of type TElement of current element by its locator.

        :param child_locator: Locator of child elements relative to their parent.
        :param name: Child elements name.
        :param supplier: Delegate that defines constructor of child element in case of custom element type.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :param state: Child elements state.
        :return: List of child elements.
        """
        pass
