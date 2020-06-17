from aquality_selenium_core.configurations.abc_logger_configuration import AbcLoggerConfiguration
from aquality_selenium_core.utilities.abc_settings_file import AbcSettingsFile


class LoggerConfiguration(AbcLoggerConfiguration):
    __DEFAULT_LANGUAGE = "en"

    def __init__(self, settings_file: AbcSettingsFile):
        self.__settings_file = settings_file

    @property
    def language(self) -> str:
        return self.__settings_file.get_value_or_default("logger.language", self.__DEFAULT_LANGUAGE)
