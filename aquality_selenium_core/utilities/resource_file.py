class ResourceFile:
    def __init__(self, path_to_resource: str):
        self.__file_canonical_path = path_to_resource
        self.__file_content = self.__get_resource_file_content()

    def __get_resource_file_content(self) -> str:
        with open(self.__file_canonical_path, encoding="utf8") as raw_data:
            return raw_data.read()

    @property
    def file_content(self) -> str:
        return self.__file_content
