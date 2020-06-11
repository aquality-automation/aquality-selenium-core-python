# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Callable

from selenium.webdriver.common.by import By

from aquality_selenium_core.elements.element_state import ElementState

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
