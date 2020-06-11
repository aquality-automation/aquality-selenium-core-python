# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Callable

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.applications.application import Application
from aquality_selenium_core.configurations.element_cache_configuration import ElementCacheConfiguration
from aquality_selenium_core.elements.element_cache_handler import ElementCacheHandler
from aquality_selenium_core.elements.element_factory import ElementFactory
from aquality_selenium_core.elements.element_finder import ElementFinder
from aquality_selenium_core.elements.element_state import ElementState
from aquality_selenium_core.elements.element_state_provider import ElementStateProvider
from aquality_selenium_core.elements.parent import Parent, T
from aquality_selenium_core.localization.localized_logger import LocalizedLogger
from aquality_selenium_core.logging.logger import Logger
from aquality_selenium_core.utilities.element_action_retrier import ElementActionRetrier
from aquality_selenium_core.waitings.conditional_wait import ConditionalWait


class Element(ABC, Parent):
    """
    Base class for any custom element.
    """

    def __init__(self, locator: By, name: str, state: ElementState):
        self._locator = locator
        self._name = name
        self._state = state

    @property
    def locator(self) -> By:
        """
        Gets unique locator of element.
        :return: Element locator.
        """
        return self._locator

    @property
    def name(self) -> str:
        """
        Gets unique name of element.
        :return: Element name.
        """
        return self._name

    @property
    def state(self) -> ElementStateProvider:
        """
        Provides ability to define of element's state (whether it is displayed, exists or not)
        and respective waiting functions.
        :return: Provider to define element's state.
        """
        raise NotImplementedError

    @property
    def element(self, timeout: timedelta = None) -> WebElement:
        """
        Gets current element by specified locator.
        Default timeout is provided in TimeoutConfiguration.
        Throws NoSuchElementException if element not found.
        :return: Instance of WebElement if found.
        """
        raise NotImplementedError

    @property
    def text(self) -> str:
        """
        Gets the item text (inner text).
        :return: Text of element.
        """
        raise NotImplementedError

    def get_attribute(self, attr: str) -> str:
        """
        Gets attribute value of the element.
        :param attr: Attribute name.
        :return: Attribute value.
        """
        raise NotImplementedError

    def send_keys(self, keys: str) -> None:
        """
        Sends keys.
        :param keys: keys for sending.
        """
        raise NotImplementedError

    def click(self) -> None:
        """
        Clicks on the item.
        """
        raise NotImplementedError

    def find_child_element(self, child_locator: By, name: str = None,
                           supplier: Callable[[By, str, ElementState], T] = None,
                           state: ElementState = ElementState.DISPLAYED) -> T:
        return self._element_factory.find_child_element(self, child_locator, name, supplier, state)

    @property
    def _element_state(self):
        return self._state

    @property
    @abstractmethod
    def _application(self) -> Application:
        pass

    @property
    @abstractmethod
    def _element_factory(self) -> ElementFactory:
        pass

    @property
    @abstractmethod
    def _element_finder(self) -> ElementFinder:
        pass

    @property
    @abstractmethod
    def _element_cache_configuration(self) -> ElementCacheConfiguration:
        pass

    @property
    @abstractmethod
    def _element_action_retrier(self) -> ElementActionRetrier:
        pass

    @property
    @abstractmethod
    def _localized_logger(self) -> LocalizedLogger:
        pass

    @property
    @abstractmethod
    def _conditional_wait(self) -> ConditionalWait:
        pass

    @property
    @abstractmethod
    def _element_type(self) -> str:
        pass

    @property
    def _cache(self) -> ElementCacheHandler:
        raise NotImplementedError

    @property
    def _logger(self) -> Logger:
        raise NotImplementedError
