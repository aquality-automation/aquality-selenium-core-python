"""Module defines localization manager."""
from abc import ABC
from abc import abstractmethod


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
