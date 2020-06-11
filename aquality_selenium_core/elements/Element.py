# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from datetime import timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.applications.Application import Application
from aquality_selenium_core.configurations.ElementCacheConfiguration import ElementCacheConfiguration
from aquality_selenium_core.elements.ElementCacheHandler import ElementCacheHandler
from aquality_selenium_core.elements.ElementFactory import ElementFactory
from aquality_selenium_core.elements.ElementFinder import ElementFinder
from aquality_selenium_core.elements.ElementState import ElementState
from aquality_selenium_core.elements.ElementStateProvider import ElementStateProvider
from aquality_selenium_core.localization.LocalizedLogger import LocalizedLogger
from aquality_selenium_core.logging.Logger import Logger
from aquality_selenium_core.utilities.ElementActionRetrier import ElementActionRetrier
from aquality_selenium_core.waitings.ConditionalWait import ConditionalWait


class Element(ABC):
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
