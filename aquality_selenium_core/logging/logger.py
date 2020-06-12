# -*- coding: utf-8 -*-
import logging
import logging.config
from typing import Dict, Type, Any

from aquality_selenium_core.utilities.file_utils import FileUtils
from aquality_selenium_core.utilities.resource_file import ResourceFile


class Singleton(type):
    _instances: Dict[Type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances.update({cls: super().__call__(*args, **kwargs)})
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        self._configure_logging()
        self._logger = logging.getLogger('aquality')

    def __getattr__(self, item):
        return getattr(self._logger, item)

    @staticmethod
    def _configure_logging():
        config_file_path = ResourceFile.get_resource_path('logconfig.json')
        data = FileUtils.read_json(config_file_path)
        logging.config.dictConfig(data)
