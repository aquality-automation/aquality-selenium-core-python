"""Module defines abstraction for element finder."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from typing import Callable
from typing import cast
from typing import Dict
from typing import List
from typing import Tuple

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from aquality_selenium_core.elements.desired_state import DesiredState
from aquality_selenium_core.elements.element_state import ExistsInAnyState
from aquality_selenium_core.localization.localized_logger import AbstractLocalizedLogger
from aquality_selenium_core.waitings.conditional_wait import AbstractConditionalWait


class AbstractElementFinder(ABC):
    """Provides ability to find elements by locator and search criteria."""

    @abstractmethod
    def find_element(
        self,
        locator: Tuple[By, str],
        desired_state: Callable[[WebElement], bool] = ExistsInAnyState(),
        timeout: timedelta = cast(timedelta, None),
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
        timeout: timedelta = cast(timedelta, None),
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
        timeout: timedelta = cast(timedelta, None),
    ) -> List[WebElement]:
        """
        Find elements in desired state defined by DesiredState object.

        :param locator: element locator.
        :param desired_state: desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        pass


class ElementFinder(AbstractElementFinder):
    """Provides ability to find elements by locator and search criteria."""

    def __init__(
        self, logger: AbstractLocalizedLogger, conditional_wait: AbstractConditionalWait
    ):
        """Initialize finder with required dependencies."""
        self.__logger = logger
        self.__conditional_wait = conditional_wait

    def find_element(
        self,
        locator: Tuple[By, str],
        desired_state: Callable[[WebElement], bool] = ExistsInAnyState(),
        timeout: timedelta = cast(timedelta, None),
    ) -> WebElement:
        """
        Find element in desired state defined by callable object.

        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: Found element.
        :raises: NoSuchElementException if element was not found in time in desired state.
        """
        state = DesiredState(
            desired_state,
            "desired",
            catch_timeout_exception=False,
            raise_no_such_element_exception=True,
        )
        return self.find_elements_in_state(locator, state, timeout)[0]

    def find_elements(
        self,
        locator: Tuple[By, str],
        desired_state: Callable[[WebElement], bool] = ExistsInAnyState(),
        timeout: timedelta = cast(timedelta, None),
    ) -> List[WebElement]:
        """
        Find elements in desired state defined by callable object.

        :param locator: element locator.
        :param desired_state: desired element state as callable object.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        state = DesiredState(desired_state, "desired", catch_timeout_exception=True)
        return self.find_elements_in_state(locator, state, timeout)

    def find_elements_in_state(
        self,
        locator: Tuple[By, str],
        desired_state: DesiredState,
        timeout: timedelta = cast(timedelta, None),
    ) -> List[WebElement]:
        """
        Find elements in desired state defined by DesiredState object.

        :param locator: element locator.
        :param desired_state: desired element state.
        :param timeout: timeout for search.
        :return: List of found elements.
        """
        elements: Dict[str, List] = {"found": [], "result": []}

        try:

            def find_elements_func(driver: WebDriver):
                elements["found"] = driver.find_elements(*locator)
                elements["result"] = list(
                    filter(desired_state.element_state_condition, elements["found"])
                )
                return any(elements["result"])

            self.__conditional_wait.wait_for_with_driver(find_elements_func, timeout)
        except TimeoutException as exception:
            self._handle_timeout_exception(
                exception, locator, desired_state, elements["found"]
            )
        return elements["result"]

    def _handle_timeout_exception(
        self,
        exception: TimeoutException,
        locator: Tuple[By, str],
        desired_state: DesiredState,
        found_elements: List[WebElement],
    ) -> None:
        message = f"No elements with locator '{locator}'' were found in {desired_state.state_name} state"
        if desired_state.catch_timeout_exception:
            if not any(found_elements):
                if desired_state.raise_no_such_element_exception:
                    raise NoSuchElementException(message)
                self.__logger.debug(
                    "loc.no.elements.found.in.state",
                    "",
                    locator,
                    desired_state.state_name,
                )
            else:
                self.__logger.debug(
                    "loc.elements.were.found.but.not.in.state",
                    "",
                    locator,
                    desired_state.state_name,
                )
        else:
            message = f"{exception.msg}: {message}"
            if desired_state.raise_no_such_element_exception and not any(
                found_elements
            ):
                raise NoSuchElementException(message)
            raise TimeoutException(message)
