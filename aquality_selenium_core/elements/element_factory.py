"""Module defines abstraction for factory of elements."""
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.element import AbstractElement
from aquality_selenium_core.elements.element_state import Displayed
from aquality_selenium_core.elements.elements_count import ElementsCount
from aquality_selenium_core.elements.parent import TElement


class AbstractElementFactory(ABC):
    """Defines the interface used to create the elements."""

    @abstractmethod
    def get_custom_element(
        self,
        supplier: Callable[
            [Tuple[By, str], str, Callable[[WebElement], bool]], TElement
        ],
        locator: Tuple[By, str],
        name: str,
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> TElement:
        """
        Create custom element according to passed parameters.

        :param supplier: Delegate that defines constructor of element.
        :param locator: Locator of the target element.
        :param name: Name of the target element.
        :param state: State of the target element.
        :return: Instance of custom element.
        """
        pass

    @abstractmethod
    def find_child_element(
        self,
        parent_element: AbstractElement,
        child_locator: Tuple[By, str],
        name: str,
        supplier: Callable[
            [Tuple[By, str], str, Callable[[WebElement], bool]], TElement
        ],
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> TElement:
        """
        Find child element by its locator relative to parent element.

        :param parent_element: Parent element.
        :param child_locator: Locator of child element relative to its parent.
        :param name: Child element name.
        :param supplier: Delegate that defines constructor of element in case of custom element.
        :param state: Child element state.
        :return: Instance of child element.
        """
        pass

    @abstractmethod
    def find_child_elements(
        self,
        parent_element: AbstractElement,
        child_locator: Tuple[By, str],
        name: str,
        supplier: Callable[
            [Tuple[By, str], str, Callable[[WebElement], bool]], TElement
        ],
        expected_count: ElementsCount = ElementsCount.ANY,
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> List[TElement]:
        """
        Find child element by its locator relative to parent element.

        :param parent_element: Parent element.
        :param child_locator: Locator of child element relative to its parent.
        :param name: Child element name.
        :param supplier: Delegate that defines constructor of element in case of custom element.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :param state: Child element state.
        :return: Instance of child element.
        """
        pass

    @abstractmethod
    def find_elements(
        self,
        locator: Tuple[By, str],
        name: str,
        supplier: Callable[
            [Tuple[By, str], str, Callable[[WebElement], bool]], TElement
        ],
        expected_count: ElementsCount = ElementsCount.ANY,
        state: Callable[[WebElement], bool] = Displayed(),
    ) -> TElement:
        """
        Find list of elements by base locator.

        :param locator: Base elements locator.
        :param name: Elements name.
        :param supplier: Delegate that defines constructor of element in case of custom elements.
        :param expected_count: Expected number of elements that have to be found (zero, more than zero, any).
        :param state: Elements state.
        :return: List of elements that found by locator.
        """
        pass
