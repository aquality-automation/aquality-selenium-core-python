"""Module defines retry policy configuration."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta


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
    def __init__(self, settings_file: AbstractSettingsFile):
        self.__settings_file = settings_file
        self.__number = self.__settings_file.get_value("retry.number")
        self.__polling_interval = Duration(
            seconds=self.__settings_file.get_value("retry.pollingInterval")
        )

    @property
    def number(self) -> int:
        return self.__number

    @property
    def polling_interval(self) -> timedelta:
        return self.__polling_interval
