"""Module defines abstraction for element cache configuration."""
from abc import ABC


class AbstractElementCacheConfiguration(ABC):
    """Provides element's cache configuration."""

    pass


class ElementCacheConfiguration(AbstractElementCacheConfiguration):
    __IS_ENABLED_PATH = "elementCache.isEnabled"

    def __init__(self, settings_file: AbcSettingsFile):
        self.__enabled: bool = settings_file.is_value_present(self.__IS_ENABLED_PATH) \
                               and bool(settings_file.get_value(self.__IS_ENABLED_PATH))

    @property
    def enabled(self) -> bool:
        return self.__enabled
