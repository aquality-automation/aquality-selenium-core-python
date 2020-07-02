"""Module defines abstraction for localization logger."""
import logging
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.localization.localization_manager import (
    AbstractLocalizationManager,
)


class AbstractLocalizedLogger(ABC):
    """Log messages in current language."""

    @abstractmethod
    def info_element_action(
        self, element_type: str, element_name: str, message_key: str, *args, **kwargs
    ) -> None:
        """
        Log localized message for action with INFO level which is applied for element.

        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def info(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with INFO level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def debug(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with DEBUG level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def warning(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with WARN level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def error(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with ERROR level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def fatal(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with FATAL(exception) level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        pass


class LocalizedLogger(AbstractLocalizedLogger):
    """This logger is used to log messages translated into language from configuration."""

    def __init__(self, localization_manager: AbstractLocalizationManager):
        """Initialize with localization manager and logger."""
        self.__localization_manager = localization_manager

    def info_element_action(
        self, element_type: str, element_name: str, message_key: str, *args, **kwargs
    ) -> None:
        """
        Log localized message for action with INFO level which is applied for element.

        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        message = f"{element_type} '{element_name}' :: {self.__localize_message(message_key, *args)}"
        logging.info(message, **kwargs)

    def info(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with INFO level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        logging.info(self.__localize_message(message_key, *args), **kwargs)

    def debug(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with DEBUG level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        logging.debug(self.__localize_message(message_key, *args), **kwargs)

    def warning(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with WARN level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        logging.warning(self.__localize_message(message_key, *args), **kwargs)

    def error(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with ERROR level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        logging.error(self.__localize_message(message_key, *args), **kwargs)

    def fatal(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with FATAL(exception) level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        logging.fatal(self.__localize_message(message_key, *args), **kwargs)

    def __localize_message(self, message_key: str, *args) -> str:
        return self.__localization_manager.get_localized_message(message_key, *args)
