"""Module defines elements state object."""
from typing import Callable

from selenium.webdriver.remote.webelement import WebElement


class DesiredState:
    """Defines desired state for element with ability to handle exceptions."""

    def __init__(
        self,
        element_state_condition: Callable[[WebElement], bool],
        state_name: str,
        catch_timeout_exception: bool = False,
        raise_no_such_element_exception: bool = False,
    ):
        """Initialize state with required dependencies."""
        self.__element_state_condition = element_state_condition
        self.__state_name = state_name
        self.__catch_timeout_exception = catch_timeout_exception
        self.__raise_no_such_element_exception = raise_no_such_element_exception

    @property
    def element_state_condition(self) -> Callable[[WebElement], bool]:
        """Get element desired state condition."""
        return self.__element_state_condition

    @property
    def state_name(self) -> str:
        """Get desired state name."""
        return self.__state_name

    @property
    def catch_timeout_exception(self) -> bool:
        """Whether to catch TimeoutException or not."""
        return self.__catch_timeout_exception

    @property
    def raise_no_such_element_exception(self) -> bool:
        """Whether to raise NoSuchElementException or not."""
        return self.__raise_no_such_element_exception
