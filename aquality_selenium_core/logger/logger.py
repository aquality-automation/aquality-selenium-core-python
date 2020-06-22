"""Module defines wrapper for logging."""
import logging.config
from logging import Handler
from typing import Any
from typing import Dict

from aquality_selenium_core.utilities.file_utils import FileUtils
from aquality_selenium_core.utilities.resource_file import ResourceFile


class Singleton(type):
    """Class defines Singleton object."""

    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        """Find existing instance or create a new one."""
        if cls not in cls._instances:
            cls._instances.update({cls: super().__call__(*args, **kwargs)})
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    """Singleton class, which defines core logger with config from logconfig.json."""

    def __init__(self):
        """Read config from file and initialize "aquality" logger."""
        self._configure_logging()
        self._logger = logging.getLogger("aquality")

    @staticmethod
    def _configure_logging():
        config_file_path = ResourceFile.get_resource_path("logconfig.json")
        data = FileUtils.read_json(config_file_path)
        logging.config.dictConfig(data)

    def add_handler(self, handler: Handler) -> None:
        """Add additional handler to "aquality" logger."""
        self._logger.addHandler(handler)

    def remove_handler(self, handler: Handler) -> None:
        """Remove handler from "aquality" logger."""
        self._logger.removeHandler(handler)

    def __getattr__(self, item):
        """Get object attribute. Delegate to initialized logger instance if attribute is not defined."""
        return getattr(self._logger, item)
