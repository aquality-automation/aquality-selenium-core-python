from datetime import timedelta

from hamcrest import assert_that, calling, raises, equal_to

from aquality_selenium_core.configurations.retry_configuration import AbstractRetryConfiguration
from aquality_selenium_core.utilities.action_retrier import AbstractActionRetrier, ActionRetrier


class TestActionRetries:
    def test__do_with_retry__should_raise_error_if_there_are_no_handled_exceptions(self):
        def func():
            raise CustomException()

        assert_that(
            calling(self.__get_action_retrier().do_with_retry).with_args(func),
            raises(CustomException),
            "Custom exception is not raised",
        )

    def test__do_with_retry__should_be_possible_to_ignore_custom_exception(self):
        raise_exception = {"value": True}

        def func():
            if raise_exception["value"]:
                raise_exception["value"] = False
                raise CustomException()
            return True

        assert_that(
            self.__get_action_retrier().do_with_retry(func, handled_exceptions=[CustomException]),
            equal_to(True),
            "Exception is raised",
        )

    def test__do_with_retry__should_not_raise_exception_when_it_is_not_raised(self):
        def func():
            return False

        assert_that(
            self.__get_action_retrier().do_with_retry(func),
            equal_to(False),
            "Action is not completed",
        )

    @staticmethod
    def __get_action_retrier() -> AbstractActionRetrier:
        timeout_configuration = CustomRetryConfiguration()
        return ActionRetrier(timeout_configuration)


class CustomException(Exception):
    pass


class CustomRetryConfiguration(AbstractRetryConfiguration):
    @property
    def number(self) -> int:
        return 2

    @property
    def polling_interval(self) -> timedelta:
        return timedelta(milliseconds=500)
