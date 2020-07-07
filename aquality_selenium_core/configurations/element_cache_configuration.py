"""Module defines abstraction for element cache configuration."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


class AbstractElementCacheConfiguration(ABC):
    """Provides element's cache configuration."""

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        """Is element caching allowed or not."""
        pass


class ElementCacheConfiguration(AbstractElementCacheConfiguration):
    """Provides element's cache configuration."""

    __IS_ENABLED_PATH = "elementCache.isEnabled"

    def __init__(self, settings_file: AbstractSettingsFile):
        """Initialize configuration with settings file."""
        self.__settings_file = settings_file

    @property
    def is_enabled(self) -> bool:
        """Is element caching allowed or not."""
        return self.__settings_file.is_value_present(self.__IS_ENABLED_PATH) and bool(
            self.__settings_file.get_value(self.__IS_ENABLED_PATH)
        )
