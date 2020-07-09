from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import is_not
from hamcrest import none

from aquality_selenium_core.configurations.logger_configuration import (
    AbstractLoggerConfiguration,
)
from aquality_selenium_core.localization.localization_manager import LocalizationManager


class TestLocalizationManager:
    def test_should_be_possible_to_get_value_by_key(self):
        assert_that(
            self.__get_localization_manager().get_localized_message("loc.clicking"),
            is_not(none()),
            "Not possible to get value from localization file",
        )

    def test_should_not_raise_error_if_key_does_not_exist(self):
        test_key = "not.existing.key"
        assert_that(
            self.__get_localization_manager().get_localized_message(test_key),
            equal_to(test_key),
            "Not possible to request not existing key",
        )

    @staticmethod
    def __get_localization_manager():
        logger_configuration = LoggerConfiguration()
        return LocalizationManager(logger_configuration)


class LoggerConfiguration(AbstractLoggerConfiguration):
    @property
    def language(self) -> str:
        return "en"

    @property
    def log_page_source(self) -> bool:
        return True
