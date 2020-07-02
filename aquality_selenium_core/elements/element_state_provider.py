"""Module defines abstraction for element state."""
from abc import ABC
from abc import abstractmethod


class AbstractElementStateProvider(ABC):
    """
    Provides ability to define of element's state (whether it is displayed, exist or not).

    Also provides respective positive and negative waiting functions.
    """

    @property
    @abstractmethod
    def is_displayed(self) -> bool:
        """
        Get element's displayed state.

        :return: true if displayed and false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_exist(self) -> bool:
        """
        Get element's exist state.

        :return: true if element exists in DOM (without visibility check) and false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        """
        Get element's Enabled state, which means element is Enabled and does not have "disabled" class.

        :return: true if enabled, false otherwise.
        """
        pass

    @property
    @abstractmethod
    def is_clickable(self) -> bool:
        """
        Get element's clickable state, which means element is displayed and enabled.

        :return: true if element is clickable, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_displayed(self, timeout: int = 0) -> bool:
        """
        Wait for element is not displayed on the page.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element is not displayed after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element exists in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_not_exist(self, timeout: int = 0) -> bool:
        """
        Wait for element does not exist in DOM (without visibility check).

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: true if element does not exist after waiting, false otherwise.
        """
        pass

    @abstractmethod
    def wait_for_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element has enabled state which means element is Enabled and does not have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_not_enabled(self, timeout: int = 0) -> bool:
        """
        Wait for element does not have enabled state which means element is not Enabled or does have "disabled" class.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :return: True if not enabled, false otherwise.
        :raises: NoSuchElementException when timeout exceeded and element not found.
        """
        pass

    @abstractmethod
    def wait_for_clickable(self, timeout: int = 0) -> None:
        """
        Wait for element to become clickable which means element is displayed and enabled.

        :param timeout: Timeout for waiting. Default value is taken from TimeoutConfiguration.
        :raises: WebDriverTimeoutException when timeout exceeded and element is not clickable.
        """
        pass
