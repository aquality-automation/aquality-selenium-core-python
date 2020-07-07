"""Module defines work with settings file."""
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List


class AbstractSettingsFile(ABC):
    """Abstract class which defines work with settings file."""

    @abstractmethod
    def get_value(self, path: str) -> Any:
        """
        Get single value by specified path from settings file.

        :param path: Path to value.
        :return: Value from file.
        """
        pass

    @abstractmethod
    def get_list(self, path: str) -> List[str]:
        """
        Get list of values by specified path from settings file.

        :param path: Path to list.
        :return: List of values from file.
        """
        pass

    @abstractmethod
    def get_dictionary(self, path: str) -> Dict[str, Any]:
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
