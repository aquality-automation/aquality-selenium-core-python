"""Module defines work with getting data from files."""


class ResourceFile:
    """Class, which defines getting data from file."""

    def __init__(self, path_to_resource: str):
        """Initialize resource file by provided path."""
        self.__file_canonical_path = path_to_resource
        self.__file_content = self.__get_resource_file_content()

    def __get_resource_file_content(self) -> str:
        with open(self.__file_canonical_path, encoding="utf8") as raw_data:
            return raw_data.read()

    @property
    def file_content(self) -> str:
        """
        Return file content.

        :return: File content.
        """
        return self.__file_content
