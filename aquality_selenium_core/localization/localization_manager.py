"""Module defines localization manager."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.configurations.logger_configuration import (
    AbstractLoggerConfiguration,
)
from aquality_selenium_core.logger.logger import Logger


class AbstractLocalizationManager(ABC):
    """This abstraction is used for translation messages to different languages."""

    @abstractmethod
    def get_localized_message(self, message_key: str, *args) -> str:
        """
        Get localized message from resources by its key.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :return: Localized message.
        """
        pass


class LocalizationManager(AbstractLocalizationManager):
    """This manager is used for translation messages to different languages."""

    def __init__(
        self, logger_configuration: AbstractLoggerConfiguration, logger: Logger
    ):
        """Initialize manager with configuration and logger."""
        self.__logger_configuration = logger_configuration
        self.__logger = logger
        self.__localization_resource_name = ""  # TODO: implement me

    def get_localized_message(self, message_key: str, *args) -> str:
        """
        Get localized message from resources by its key.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :return: Localized message.
        """
        raise NotImplementedError
        self.__logger.warn(
            "Cannot find localized message by key '%s' in resource file '%s'",
            message_key,
            self.__localization_resource_name,
        )
        return message_key
