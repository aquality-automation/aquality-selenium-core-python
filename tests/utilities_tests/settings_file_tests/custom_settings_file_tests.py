from typing import Any
from typing import Dict
from typing import List

from hamcrest import assert_that

from aquality_selenium_core.utilities.abstract_settings_file import AbstractSettingsFile


class TestCustomSettingsFile:
    def test_should_be_possible_to_override_settings_file(self):
        custom_implementation: AbstractSettingsFile = CustomSettingsFile()
        value = custom_implementation.get_value("timeouts.timeoutPollingInterval")
        assert_that(value is None, "Value should be got from CustomSettingsFile")


class CustomSettingsFile(AbstractSettingsFile):
    def get_value(self, path: str) -> Any:
        pass

    def get_list(self, path: str) -> List[str]:
        pass

    def get_dictionary(self, path: str) -> Dict[str, Any]:
        pass

    def is_value_present(self, path: str) -> bool:
        pass
