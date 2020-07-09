"""Module defines work with settings file."""
import json
import logging
import os
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional

from jsonpath_ng import DatumInContext
from jsonpath_ng import parse

from aquality_selenium_core.utilities.resource_file import ResourceFile


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

    def get_value_or_default(self, path: str, default: Any) -> Any:
        """
        Get single value by specified path from settings file or default if not present.

        :param path: Path to value.
        :param default: Default value.
        :return: Value from file or default if not present.
        """
        return self.get_value(path) if self.is_value_present(path) else default

    @abstractmethod
    def get_list(self, path: str) -> List[Any]:
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


class JsonSettingsFile(AbstractSettingsFile):
    """Class which defines work with .json settings file."""

    def __init__(self, resource_name: str, root_dir: str = cast(str, None)):
        """Initialize work with .json setting file by provided path."""
        self.__resource_file = ResourceFile(resource_name, root_dir)
        self.__content = json.loads(self.__resource_file.file_content)

    def get_value(self, path: str) -> Any:
        """
        Get single value by specified path from environment variables or settings file.

        Throws IllegalArgumentException if nothing was found
        :param path: Path to value.
        :return: Value by specified path.
        """
        return self.__get_env_value_or_default(path, throw_if_empty=True)

    def get_list(self, path: str) -> List[Any]:
        """
        Get list of values by specified path from environment variables or settings file.

        :param path: Path to value.
        :return: List of values by specified path.
        :raises: ValueError if nothing is found.
        """
        env_var = self.__get_env_value(path)
        data = (
            env_var.split(",")
            if env_var
            else self.__get_json_node(path, throw_if_empty=True)[0].value
        )
        return [value.strip() for value in data]

    def get_dictionary(self, path: str) -> Dict[str, Any]:
        """
        Get dictionary of values by specified path from settings file.

        :param path: Path to value.
        :return: Dictionary of values by specified path.
        :raises: ValueError if nothing is found.
        """
        node = self.__get_json_node(path, throw_if_empty=True)
        return {key: self.get_value(f"{path}.{key}") for key in node[0].value}

    def is_value_present(self, path: str) -> bool:
        """
        Check that value present in settings file or environment variables.

        :param path: Path to value.
        :return: Presence of value.
        """
        return (
            self.__get_env_value(path) is not None
            or len(self.__get_json_node(path, throw_if_empty=False)) > 0
        )

    def __get_env_value_or_default(
        self, json_path: str, throw_if_empty: bool = False
    ) -> Any:
        env_var = self.__get_env_value(json_path)
        node = self.__get_json_node(json_path, throw_if_empty and not env_var)
        return self.__use_env_value_or_default(node, env_var) if node else env_var

    @staticmethod
    def __use_env_value_or_default(node: List[DatumInContext], env_value: Any) -> Any:
        node_value: Any = node[0].value
        return env_value if env_value else node_value

    def __get_json_node(
        self, json_path: str, throw_if_empty: bool
    ) -> List[DatumInContext]:
        node: List[DatumInContext] = parse(f"$.{json_path}").find(self.__content)
        if not node and throw_if_empty:
            raise ValueError(
                f"Json field by json-path {json_path} was not found in the file {self.__content}"
            )
        return node

    @staticmethod
    def __get_env_value(json_path: str) -> Optional[str]:
        env_var = os.getenv(json_path)
        if env_var:
            logging.debug(
                f"***** Using variable passed from environment {json_path}={env_var}"
            )
        return env_var
