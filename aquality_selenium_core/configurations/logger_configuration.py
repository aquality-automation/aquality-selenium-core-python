"""Module defines logger configuration."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractLoggerConfiguration(ABC):
    """Describes logger configuration."""

    @property
    @abstractmethod
    def language(self) -> str:
        """Get language of framework."""
        pass

    @property
    @abstractmethod
    def log_page_source(self) -> bool:
        """Perform page source logging in case of catastrophic failures or not."""
        pass


class LoggerConfiguration(AbstractLoggerConfiguration):
    __DEFAULT_LANGUAGE = "en"
    __DEFAULT_LOG_VALUE = True

    def __init__(self, settings_file: AbstractSettingsFile):
        """Initialize configuration with settings file."""
        self.__settings_file = settings_file

    @property
    def language(self) -> str:
        """Get language of framework."""
        return self.__settings_file.get_value_or_default(
            "logger.language", self.__DEFAULT_LANGUAGE
        )

    @property
    def log_page_source(self) -> bool:
        """Perform page source logging in case of catastrophic failures or not."""
        return bool(
            self.__settings_file.get_value_or_default(
                "logger.logPageSource", self.__DEFAULT_LANGUAGE
            )
        )
