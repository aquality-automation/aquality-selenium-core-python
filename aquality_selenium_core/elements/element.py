"""Abstraction for any custom element of the web, desktop of mobile application."""
from abc import ABC
from abc import abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.applications.application import AbstractApplication
from aquality_selenium_core.configurations.element_cache_configuration import (
    AbstractElementCacheConfiguration,
)
from aquality_selenium_core.elements.element_cache_handler import (
    AbstractElementCacheHandler,
)
from aquality_selenium_core.elements.element_factory import AbstractElementFactory
from aquality_selenium_core.elements.element_finder import AbstractElementFinder
from aquality_selenium_core.elements.element_state import ElementState
from aquality_selenium_core.elements.element_state_provider import (
    AbstractElementStateProvider,
)
from aquality_selenium_core.localization.localized_logger import AbstractLocalizedLogger
from aquality_selenium_core.utilities.element_action_retrier import (
    AbstractElementActionRetrier,
)
from aquality_selenium_core.waitings.conditional_wait import AbstractConditionalWait


class AbstractElement(ABC):
    """Base class for any custom element."""

    def __init__(self, locator: By, name: str, state: ElementState):
        """Initialize element with locator, name and state."""
        self._locator = locator
        self._name = name
        self._state = state

    @property
    def locator(self) -> By:
        """
        Get unique locator of element.

        :return: Element locator.
        """
        return self._locator

    @property
    def name(self) -> str:
        """
        Get unique name of element.

        :return: Element name.
        """
        return self._name

    @property
    def state(self) -> AbstractElementStateProvider:
        """
        Get element state provider.

        Provider allows to define element's state (whether it is displayed, exists or not).
        :return: Provider to define element's state.
        """
        raise NotImplementedError

    @property
    def text(self) -> str:
        """
        Get text of item (inner text).

        :return: Text of element.
        """
        raise NotImplementedError

    def element(self, timeout: int = 0) -> WebElement:
        """
        Get current element by specified locator.

        Default timeout is provided in TimeoutConfiguration.
        Throws NoSuchElementException if element not found.
        :return: Instance of WebElement if found.
        """
        raise NotImplementedError

    def get_attribute(self, attr: str) -> str:
        """
        Get attribute value of the element.

        :param attr: Attribute name.
        :return: Attribute value.
        """
        raise NotImplementedError

    def send_keys(self, keys: str) -> None:
        """
        Send keys.

        :param keys: keys for sending.
        """
        raise NotImplementedError

    def click(self) -> None:
        """Click on the item."""
        raise NotImplementedError

    @property
    def _element_state(self):
        return self._state

    @property
    @abstractmethod
    def _application(self) -> AbstractApplication:
        pass

    @property
    @abstractmethod
    def _element_factory(self) -> AbstractElementFactory:
        pass

    @property
    @abstractmethod
    def _element_finder(self) -> AbstractElementFinder:
        pass

    @property
    @abstractmethod
    def _element_cache_configuration(self) -> AbstractElementCacheConfiguration:
        pass

    @property
    @abstractmethod
    def _element_action_retrier(self) -> AbstractElementActionRetrier:
        pass

    @property
    @abstractmethod
    def _localized_logger(self) -> AbstractLocalizedLogger:
        pass

    @property
    @abstractmethod
    def _conditional_wait(self) -> AbstractConditionalWait:
        pass

    @property
    @abstractmethod
    def _element_type(self) -> str:
        pass

    @property
    def _cache(self) -> AbstractElementCacheHandler:
        raise NotImplementedError
