"""Module defines work with settings file."""
from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import TypeVar

T = TypeVar("T")


class AbstractSettingsFile(ABC):
    """Abstract class which defines work with settings file."""

    @abstractmethod
    def get_value(self, path: str) -> T:
        """
        Get single value by specified path from settings file.

        :param path: Path to value.
        :return: Value from file.
        """
        pass

    @abstractmethod
    def get_value_or_default(self, path: str, default: T) -> T:
        """
        Get single value by specified path from settings file or default if not present.

        :param path: Path to value.
        :param default: Default value.
        :return: Value from file or default if not present.
        """
        pass

    @abstractmethod
    def get_list(self, path: str) -> List[T]:
        """
        Get list of values by specified path from settings file.

        :param path: Path to list.
        :return: List of values from file.
        """
        pass

    @abstractmethod
    def get_dictionary(self, path: str) -> Dict[str, T]:
        """
        Get dictionary of values by specified path from settings file.

        :param path: Path to dictionary.
        :return: Dictionary of values from file.
        """
        pass

    @abstractmethod
    def is_value_present(self, path: str) -> bool:
        """
        Check that value present in settings file.

        :param path: Path to value.
        :return: Presence of value.
        """
        pass
