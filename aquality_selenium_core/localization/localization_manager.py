"""Module defines localization manager."""
import logging
import os
from abc import ABC
from abc import abstractmethod
from typing import cast

from aquality_selenium_core.configurations.logger_configuration import (
    AbstractLoggerConfiguration,
)
from aquality_selenium_core.utilities.resource_file import ResourceFile
from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.settings_file import JsonSettingsFile


class AbstractLocalizationManager(ABC):
    """This abstraction is used for translation messages to different languages."""

    @abstractmethod
    def get_localized_message(self, message_key: str, *message_args) -> str:
        """
        Get localized message from resources by its key.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :return: Localized message.
        """
        pass


class LocalizationManager(AbstractLocalizationManager):
    """Get messages translated to different languages based on configuration."""

    def __init__(self, logger_configuration: AbstractLoggerConfiguration):
        """Initialize manager with configuration."""
        language = logger_configuration.language
        self.__core_localization_file = self.__get_localization_file(
            f"core.{language}.json"
        )
        self.__localization_file = self.__get_localization_file(f"{language}.json")

    @staticmethod
    def __get_localization_file(file_name: str) -> AbstractSettingsFile:
        path = os.path.join("localization", file_name)
        return (
            JsonSettingsFile(path)
            if ResourceFile(path).exists
            else cast(AbstractSettingsFile, None)
        )

    def get_localized_message(self, message_key: str, *message_args) -> str:
        """
        Get localized message from resources by its key.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :return: Localized message.
        """
        json_path = f'"{message_key}"'
        localized_message = message_key
        if self.__localization_file and self.__localization_file.is_value_present(
            json_path
        ):
            localized_message = self.__localization_file.get_value(json_path)
        elif self.__core_localization_file.is_value_present(json_path):
            localized_message = self.__core_localization_file.get_value(json_path)
        else:
            logging.warning(f"Cannot find localized message by key '{message_key}'.")
        return localized_message % message_args
