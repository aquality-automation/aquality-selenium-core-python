"""Module defines timeouts configuration."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractTimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""

    @property
    @abstractmethod
    def implicit(self) -> timedelta:
        """Get WedDriver ImplicitWait timeout."""
        pass

    @property
    @abstractmethod
    def condition(self) -> timedelta:
        """Get default ConditionalWait timeout."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> timedelta:
        """Get ConditionalWait polling interval."""
        pass

    @property
    @abstractmethod
    def command(self) -> timedelta:
        """Get WebDriver Command timeout."""
        pass


class TimeoutConfiguration(AbstractTimeoutConfiguration):
    """Abstraction for timeout configuration."""

    def __init__(self, settings_file: AbstractSettingsFile):
        """Initialize configuration with settings file."""
        self.__settings_file = settings_file

    @property
    def implicit(self) -> timedelta:
        """Get WedDriver ImplicitWait timeout."""
        return timedelta(seconds=self.__get_timeout("timeouts.timeoutImplicit"))

    @property
    def condition(self) -> timedelta:
        """Get default ConditionalWait timeout."""
        return timedelta(seconds=self.__get_timeout("timeouts.timeoutCondition"))

    @property
    def polling_interval(self) -> timedelta:
        """Get ConditionalWait polling interval."""
        return timedelta(
            milliseconds=self.__get_timeout("timeouts.timeoutPollingInterval")
        )

    @property
    def command(self) -> timedelta:
        """Get WebDriver Command timeout."""
        return timedelta(seconds=self.__get_timeout("timeouts.timeoutCommand"))

    def __get_timeout(self, key: str) -> int:
        return int(self.__settings_file.get_value(key))
