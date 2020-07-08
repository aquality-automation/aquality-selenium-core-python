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
        config_value = self.__get_config_value("timeouts.timeoutImplicit")
        return timedelta(seconds=config_value)

    @property
    def condition(self) -> timedelta:
        """Get default ConditionalWait timeout."""
        config_value = self.__get_config_value("timeouts.timeoutCondition")
        return timedelta(seconds=config_value)

    @property
    def polling_interval(self) -> timedelta:
        """Get ConditionalWait polling interval."""
        config_value = self.__get_config_value("timeouts.timeoutPollingInterval")
        return timedelta(milliseconds=config_value)

    @property
    def command(self) -> timedelta:
        """Get WebDriver Command timeout."""
        config_value = self.__get_config_value("timeouts.timeoutCommand")
        return timedelta(seconds=config_value)

    def __get_config_value(self, key: str) -> int:
        return self.__settings_file.get_value(key)
