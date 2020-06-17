from aquality_selenium_core.configurations.abc_element_cache_configuration import AbcElementCacheConfiguration
from aquality_selenium_core.utilities.abc_settings_file import AbcSettingsFile


class ElementCacheConfiguration(AbcElementCacheConfiguration):
    __IS_ENABLED_PATH = "elementCache.isEnabled"

    def __init__(self, settings_file: AbcSettingsFile):
        self.__enabled: bool = settings_file.is_value_present(self.__IS_ENABLED_PATH) \
                               and bool(settings_file.get_value(self.__IS_ENABLED_PATH))

    @property
    def enabled(self) -> bool:
        return self.__enabled
