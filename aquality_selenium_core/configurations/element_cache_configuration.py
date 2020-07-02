"""Module defines abstraction for element cache configuration."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractElementCacheConfiguration(ABC):
    """Provides element's cache configuration."""

    @property
    @abstractmethod
    def enabled(self) -> bool:
        pass


class ElementCacheConfiguration(AbstractElementCacheConfiguration):
    __IS_ENABLED_PATH = "elementCache.isEnabled"

    def __init__(self, settings_file: AbstractSettingsFile):
        self.__enabled: bool = settings_file.is_value_present(
            self.__IS_ENABLED_PATH
        ) and bool(settings_file.get_value(self.__IS_ENABLED_PATH))

    @property
    def enabled(self) -> bool:
        return self.__enabled
