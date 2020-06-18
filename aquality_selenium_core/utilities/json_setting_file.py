import json
import logging
import os
from typing import List, Any, Dict, Optional

from jsonpath_ng import parse

from aquality_selenium_core.exceptions.illegal_argument_exception import IllegalArgumentException
from aquality_selenium_core.utilities.abstract_settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.resource_file import ResourceFile


class JsonSettingsFile(AbstractSettingsFile):

    def __init__(self, resource_name: str):
        self.__resource_file = ResourceFile(resource_name)
        self.__content = json.loads(self.__resource_file.file_content)

    def get_value(self, path: str) -> Any:
        return self.__get_env_value_or_default(path, True)

    def get_list(self, path: str) -> List[str]:
        env_var = self.__get_env_value(path)
        data = env_var.split(',') if env_var else self.__get_json_node(path, throw_if_empty=True)[0].value
        return [value.strip() for value in data]

    def get_dictionary(self, path: str) -> Dict[str, Any]:
        node = self.__get_json_node(path, throw_if_empty=True)
        return {key: self.get_value(f'{path}.{key}') for key in node[0].value}

    def is_value_present(self, path: str) -> bool:
        return self.__get_env_value(path) is not None or len(self.__get_json_node(path, throw_if_empty=False)) > 0

    def __get_env_value_or_default(self, json_path: str, throw_if_empty: bool = False) -> Any:
        env_var = self.__get_env_value(json_path)
        node = self.__get_json_node(json_path, throw_if_empty and not env_var)
        return self.__use_env_value_or_default(node, env_var) if node else env_var

    @staticmethod
    def __use_env_value_or_default(node, env_value):
        return node[0].value if not env_value else env_value

    def __get_json_node(self, json_path: str, throw_if_empty: bool) -> Any:
        node = parse(f'$.{json_path}').find(self.__content)
        if not node and throw_if_empty:
            raise IllegalArgumentException(
                f'Json field by json-path {json_path} was not found in the file {self.__content}')
        return node

    @staticmethod
    def __get_env_value(json_path: str) -> Optional[str]:
        env_var = os.getenv(json_path)
        if env_var:
            logging.debug(f'***** Using variable passed from environment {json_path}={env_var}')
        return env_var
