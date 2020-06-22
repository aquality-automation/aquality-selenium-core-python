"""Utilities for operations with files."""
import json
from typing import Any


class FileUtils:
    """Util class for operation with files."""

    @staticmethod
    def read_json(file_path: str) -> Any:
        """
        Read data from JSON file into dictionary.

        :param file_path: Path to JSON file.
        :return: Deserialized JSON document into dictionary.
        """
        with open(file_path) as raw_data:
            return json.loads(raw_data.read())
