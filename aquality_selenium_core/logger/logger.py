"""Module defines wrapper for logging."""
import logging.config
from logging import Handler
from typing import Any
from typing import Dict

from aquality_selenium_core.utilities.file_utils import FileUtils
from aquality_selenium_core.utilities.resource_file import ResourceFile


class Singleton(type):
    """Class defines Singleton object."""

    __instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs):
        """Find existing instance or create a new one."""
        if cls not in cls.__instances:
            cls.__instances.update({cls: super().__call__(*args, **kwargs)})
        return cls.__instances[cls]


class Logger(metaclass=Singleton):
    """Singleton class, which defines core logger with config from logconfig.json."""

    def __init__(self):
        """Read config from file and initialize "aquality" logger."""
        self.__configure_logging()
        self.__logger = logging.getLogger("aquality")

    @staticmethod
    def __configure_logging():
        config_file_path = ResourceFile.get_resource_path("logconfig.json")
        data = FileUtils.read_json(config_file_path)
        logging.config.dictConfig(data)

    def add_handler(self, handler: Handler) -> None:
        """Add additional handler to "aquality" logger."""
        self.__logger.addHandler(handler)

    def remove_handler(self, handler: Handler) -> None:
        """Remove handler from "aquality" logger."""
        self.__logger.removeHandler(handler)

    def info(self, msg: str, *args, **kwargs) -> None:
        """
        Log message with INFO level.

        :param msg: Log message:
        :param args: Arguments for message.
        :param kwargs: Arguments for logger.
        """
        self.__logger.info(msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs) -> None:
        """
        Log message with DEBUG level.

        :param msg: Log message:
        :param args: Arguments for message.
        :param kwargs: Arguments for logger.
        """
        self.__logger.debug(msg, *args, **kwargs)

    def warn(self, msg: str, *args, **kwargs) -> None:
        """
        Log message with INFO level.

        :param msg: Log message:
        :param args: Arguments for message.
        :param kwargs: Arguments for logger.
        """
        self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        """
        Log message with INFO level.

        :param msg: Log message:
        :param args: Arguments for message.
        :param kwargs: Arguments for logger.
        """
        self.__logger.error(msg, *args, **kwargs)

    def fatal(self, msg: str, *args, **kwargs) -> None:
        """
        Log message with INFO level.

        :param msg: Log message:
        :param args: Arguments for message.
        :param kwargs: Arguments for logger.
        """
        self.__logger.exception(msg, *args, exc_info=True, **kwargs)
