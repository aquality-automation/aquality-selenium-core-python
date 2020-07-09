"""Module defines work with getting data from files."""
import os
from typing import cast

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ResourceFile:
    """Class, which defines getting data from file."""

    def __init__(self, resource_name: str, root_dir: str = cast(str, None)):
        """Initialize resource file by provided path."""
        self.__resource_name = resource_name
        self.__root_dir = root_dir
        self.__file_canonical_path = self.get_resource_path(resource_name)
        self.__file_content = self.__get_resource_file_content()

    def __get_resource_file_content(self) -> str:
        with open(self.__file_canonical_path, encoding="utf8") as raw_data:
            return raw_data.read()

    def get_resource_path(self, resource_name: str) -> str:
        """
        Get path to resource by its name.

        :param resource_name: name of resource file with extension.
        :return: path to resource.
        """
        root = ROOT_DIR if self.__root_dir is None else self.__root_dir
        return os.path.join(root, "resources", resource_name)

    @property
    def file_content(self) -> str:
        """Get file content as string."""
        return self.__file_content

    @property
    def resource_name(self) -> str:
        """Get name of resource."""
        return self.__resource_name

    @property
    def file_canonical_path(self) -> str:
        """Get resource file canonical path."""
        return self.__file_canonical_path
