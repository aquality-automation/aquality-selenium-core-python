from aquality_selenium_core.configurations.abc_retry_configuration import AbcRetryConfiguration
from aquality_selenium_core.configurations.duration import Duration
from aquality_selenium_core.utilities.abc_settings_file import AbcSettingsFile


class RetryConfiguration(AbcRetryConfiguration):

    def __init__(self, settings_file: AbcSettingsFile):
        self.__settings_file = settings_file
        self.__number = self.__settings_file.get_value('retry.number')
        a = self.__settings_file.get_value('retry.pollingInterval')
        self.__polling_interval = Duration(seconds=self.__settings_file.get_value('retry.pollingInterval'))
        b = self.__polling_interval.milliseconds
        print(1)

    @property
    def number(self) -> int:
        return self.__number

    @property
    def polling_interval(self) -> Duration:
        return self.__polling_interval
