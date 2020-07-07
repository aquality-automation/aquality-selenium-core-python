"""Module defines abstraction for localization logger."""
from abc import ABC
from abc import abstractmethod

from aquality_selenium_core.configurations.logger_configuration import (
    AbstractLoggerConfiguration,
)


class AbstractLocalizedLogger(ABC):
    """Log messages in current language."""

    @abstractmethod
    def info_element_action(
        self,
        element_type: str,
        element_name: str,
        message_key: str,
        *message_args,
        **logger_kwargs
    ) -> None:
        """
        Log localized message for action with INFO level which is applied for element.

        :param element_type: Type of the element.
        :param element_name: Name of the element.
        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @property
    @abstractmethod
    def configuration(self) -> AbstractLoggerConfiguration:
        """Get logger configuration."""
        pass

    @abstractmethod
    def info(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with INFO level.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def debug(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with DEBUG level.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def warning(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with WARN level.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def error(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with ERROR level.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass

    @abstractmethod
    def fatal(self, message_key: str, *message_args, **logger_kwargs) -> None:
        """
        Log localized message with FATAL(exception) level.

        :param message_key: Key in resource file.
        :param message_args: Arguments, which will be provided to template of localized message.
        :param logger_kwargs: Arguments for logger.
        """
        pass
