"""Module defines timeouts configuration."""
from abc import ABC
from abc import abstractmethod
from enum import Enum

from aquality_selenium_core.configurations.duration import Duration
from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractTimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""

    @property
    @abstractmethod
    def implicit(self) -> int:
        """Get WedDriver ImplicitWait timeout."""
        pass

    @property
    @abstractmethod
    def condition(self) -> int:
        """Get default ConditionalWait timeout."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> int:
        """Get ConditionalWait polling interval."""
        pass

    @property
    @abstractmethod
    def command(self) -> int:
        """Get WebDriver Command timeout."""
        pass


class TimeoutConfiguration(AbstractTimeoutConfiguration):
    def __init__(self, settings_file: AbstractSettingsFile):
        self.__settings_file = settings_file
        self.__condition: Duration = self.__get_duration_from_seconds(TimeOut.CONDITION)
        self.__polling_interval: Duration = Duration(
            milliseconds=self.__get_time_out(TimeOut.POLL_INTERVAL)
        )
        self.__implicit: Duration = self.__get_duration_from_seconds(TimeOut.IMPLICIT)
        self.__command: Duration = self.__get_duration_from_seconds(TimeOut.COMMAND)

    @property
    def implicit(self) -> Duration:
        return self.__implicit

    @property
    def condition(self) -> Duration:
        return self.__condition

    @property
    def polling_interval(self) -> Duration:
        return self.__polling_interval

    @property
    def command(self) -> Duration:
        return self.__command

    def __get_time_out(self, time_out: Enum) -> int:
        return int(self.__settings_file.get_value(time_out.value))

    def __get_duration_from_seconds(self, time_out: Enum) -> Duration:
        return Duration(seconds=self.__get_time_out(time_out))


class TimeOut(Enum):
    IMPLICIT = "timeouts.timeoutImplicit"
    CONDITION = "timeouts.timeoutCondition"
    POLL_INTERVAL = "timeouts.timeoutPollingInterval"
    COMMAND = "timeouts/timeoutCommand"
