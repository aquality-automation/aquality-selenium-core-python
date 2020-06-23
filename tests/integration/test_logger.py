from logging import DEBUG
from logging import FileHandler

from hamcrest import assert_that
from hamcrest import contains_string
from hamcrest import is_not

from aquality_selenium_core.logger.logger import Logger

logger = Logger()

HANDLER_TEST_LOG_FILE_NAME = "test.log"


class TestLogger:
    file_handler = FileHandler(HANDLER_TEST_LOG_FILE_NAME)
    file_handler.setLevel(DEBUG)

    def test_should_be_possible_to_add_handler(self):
        log_message = "Add handler test message"
        logger.add_handler(self.file_handler)
        logger.info(log_message)

        log_data = self._read_file_data(HANDLER_TEST_LOG_FILE_NAME)
        assert_that(
            log_data, contains_string(log_message), "Log message not found in log file"
        )

    def test_should_be_possible_to_remove_handler(self):
        log_message = "Remove handler test message"
        logger.add_handler(self.file_handler)
        logger.remove_handler(self.file_handler)
        logger.info(log_message)

        log_data = self._read_file_data(HANDLER_TEST_LOG_FILE_NAME)
        assert_that(
            log_data,
            is_not(contains_string(log_message)),
            "Log message not found in log file",
        )

    @staticmethod
    def _read_file_data(file_name):
        with open(file_name) as file:
            return file.read()
