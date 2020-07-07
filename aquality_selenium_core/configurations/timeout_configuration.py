"""Module defines timeouts configuration."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta
from enum import Enum

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
        self.__implicit = timedelta(seconds=self.__get_timeout(TimeOut.IMPLICIT))
        self.__condition = timedelta(seconds=self.__get_timeout(TimeOut.CONDITION))
        self.__polling_interval = timedelta(
            milliseconds=self.__get_timeout(TimeOut.POLL_INTERVAL)
        )
        self.__command = timedelta(seconds=self.__get_timeout(TimeOut.COMMAND))

    def __get_timeout(self, time_out: Enum) -> int:
        return int(self.__settings_file.get_value(time_out.value))

    @property
    def implicit(self) -> timedelta:
        """Get WedDriver ImplicitWait timeout."""
        return self.__implicit

    @property
    def condition(self) -> timedelta:
        """Get default ConditionalWait timeout."""
        return self.__condition

    @property
    def polling_interval(self) -> timedelta:
        """Get ConditionalWait polling interval."""
        return self.__polling_interval

    @property
    def command(self) -> timedelta:
        """Get WebDriver Command timeout."""
        return self.__command


class TimeOut(Enum):
    IMPLICIT = "timeouts.timeoutImplicit"
    CONDITION = "timeouts.timeoutCondition"
    POLL_INTERVAL = "timeouts.timeoutPollingInterval"
    COMMAND = "timeouts/timeoutCommand"
