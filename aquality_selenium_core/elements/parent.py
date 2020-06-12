# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Callable, List

from selenium.webdriver.common.by import By

from aquality_selenium_core.elements.element_state import ElementState
from aquality_selenium_core.elements.elements_count import ElementsCount

T = TypeVar('T')


class Parent(ABC):
    """
    Defines behavior of element with child elements.
    """

    @abstractmethod
    def find_child_element(self, child_locator: By, name: str = None,
                           supplier: Callable[[By, str, ElementState], T] = None,
                           state: ElementState = ElementState.DISPLAYED) -> T:
        """
        Finds child element ot type T of current element by its locator.
        :param child_locator: Locator of child element.
        :param name: Child element name.
        :param supplier: Delegate that defines constructor of child element in case of custom element.
        :param state: Child element state.
        :return: Instance of child element.
        """
        pass

    @abstractmethod
    def find_child_elements(self, child_locator: By, name: str = None,
                            supplier: Callable[[By, str, ElementState], T] = None,
                            expected_count: ElementsCount = ElementsCount.ANY,
                            state: ElementState = ElementState.DISPLAYED) -> List[T]:
        """
        Finds child elements of current element by its locator.
        :param child_locator: Locator of child elements relative to their parent.
        :param name: Child elements name.
        :param supplier: Delegate that defines constructor of child element in case of custom element type.
        :param expected_count: Expected number of elements that have to be found (zero, more then zero, any).
        :param state: Child elements state.
        :return: List of child elements.
        """
        pass
