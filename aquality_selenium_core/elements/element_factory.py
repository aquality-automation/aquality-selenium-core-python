# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Callable

from selenium.webdriver.common.by import By

from aquality_selenium_core.elements.element import Element
from aquality_selenium_core.elements.element_state import ElementState
from aquality_selenium_core.elements.elements_count import ElementsCount
from aquality_selenium_core.elements.parent import T


class ElementFactory(ABC):
    """
    Defines the interface used to create the elements.
    """

    @abstractmethod
    def get_custom_element(self, supplier: Callable[[By, str, ElementState], T], locator: By, name: str,
                           state: ElementState = ElementState.DISPLAYED) -> T:
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
    def find_child_element(self, parent_element: Element, child_locator: By, name: str = None,
                           supplier: Callable[[By, str, ElementState], T] = None,
                           state: ElementState = ElementState.DISPLAYED) -> T:
        """
        Finds child element by its locator relative to parent element.
        :param parent_element: Parent element.
        :param child_locator: Locator of child element relative to its parent.
        :param name: Delegate that defines constructor of element in case of custom element.
        :param supplier: Child element state.
        :param state: Child element name.
        :return: Instance of child element.
        """
        pass

    def find_elements(self, locator: By, name: str, supplier: Callable[[By, str, ElementState], T] = None,
                      expected_count: ElementsCount = ElementsCount.ANY,
                      state: ElementState = ElementState.DISPLAYED) -> T:
        """
        Finds list of elements by base locator.
        :param locator: Base elements locator.
        :param name: Elements name.
        :param supplier: Delegate that defines constructor of element in case of custom elements.
        :param expected_count: Expected number of elements that have to be found (zero, more then zero, any).
        :param state: Elements state.
        :return: List of elements that found by locator.
        """
        pass
