from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractLoggerConfiguration(ABC):
    @property
    @abstractmethod
    def language(self) -> str:
        pass


class LoggerConfiguration(AbstractLoggerConfiguration):
    __DEFAULT_LANGUAGE = "en"

    def __init__(self, settings_file: AbstractSettingsFile):
        self.__settings_file = settings_file

    @property
    def language(self) -> str:
        return self.__settings_file.get_value_or_default(
            "logger.language", self.__DEFAULT_LANGUAGE
        )
