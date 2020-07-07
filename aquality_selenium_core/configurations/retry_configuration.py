"""Module defines retry policy configuration."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractRetryConfiguration(ABC):
    """Describes retry configuration."""

    @property
    @abstractmethod
    def number(self) -> int:
        """Get the number of attempts to retry."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> timedelta:
        """Get the polling interval used in retry."""
        pass


class RetryConfiguration(AbstractRetryConfiguration):
    """Describes retry configuration."""

    def __init__(self, settings_file: AbstractSettingsFile):
        """Initialize configuration with settings file."""
        self.__settings_file = settings_file
        self.__number = self.__settings_file.get_value("retry.number")
        self.__polling_interval = timedelta(
            milliseconds=self.__settings_file.get_value("retry.pollingInterval")
        )

    @property
    def number(self) -> int:
        """Get the number of attempts to retry."""
        return self.__number

    @property
    def polling_interval(self) -> timedelta:
        """Get the polling interval used in retry."""
        return self.__polling_interval
