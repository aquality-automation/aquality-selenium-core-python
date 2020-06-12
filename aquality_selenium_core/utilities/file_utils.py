# -*- coding: utf-8 -*-
import json


class FileUtils:
    """
    Util class for operations with files.
    """

    @staticmethod
    def read_json(file_path: str) -> dict:
        """
        Reads data from JSON file into dictionary.
        :param file_path: Path to JSON file.
        :return: Deserialized JSON document into dictionary.
        """
        with open(file_path) as raw_data:
            return json.loads(raw_data.read())
