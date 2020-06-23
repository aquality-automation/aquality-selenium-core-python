"""Module defines abstraction for localization logger."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.localization.localization_manager import (
    AbstractLocalizationManager,
)
from aquality_selenium_core.logger.logger import Logger


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
    def warn(self, message_key: str, *args, **kwargs) -> None:
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

    def __init__(
        self, localization_manager: AbstractLocalizationManager, logger: Logger
    ):
        """Initialize with localization manager and logger."""
        self._localization_manager = localization_manager
        self._logger = logger

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
        message = f"{element_type} '{element_name}' :: {self._localize_message(message_key, *args)}"
        self._logger.info(message, **kwargs)

    def info(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with INFO level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        self._logger.info(self._localize_message(message_key, *args), **kwargs)

    def debug(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with DEBUG level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        self._logger.debug(self._localize_message(message_key, *args), **kwargs)

    def warn(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with WARN level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        self._logger.warn(self._localize_message(message_key, *args), **kwargs)

    def error(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with ERROR level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        self._logger.error(self._localize_message(message_key, *args), **kwargs)

    def fatal(self, message_key: str, *args, **kwargs) -> None:
        """
        Log localized message with FATAL(exception) level.

        :param message_key: Key in resource file.
        :param args: Arguments, which will be provided to template of localized message.
        :param kwargs: Arguments for logger.
        """
        self._logger.fatal(self._localize_message(message_key, *args), **kwargs)

    def _localize_message(self, message_key: str, *args) -> str:
        return self._localization_manager.get_localized_message(message_key, *args)
