from datetime import timedelta

from hamcrest import assert_that
from hamcrest import calling
from hamcrest import equal_to
from hamcrest import is_not
from hamcrest import raises

from aquality_selenium_core.configurations.timeout_configuration import (
    AbstractTimeoutConfiguration,
)
from aquality_selenium_core.waitings.conditional_wait import AbstractConditionalWait
from aquality_selenium_core.waitings.conditional_wait import ConditionalWait


class TestConditionalWait:
    def test__wait_for__should_raise_exception_if_it_is_not_ignored(self):
        def func():
            raise CustomException()

        assert_that(
            calling(self.__get_conditional_wait().wait_for).with_args(func),
            raises(CustomException),
            "Custom exception is not raised",
        )

    def test__wait_for__should_be_possible_to_ignore_custom_exception(self):
        def func():
            raise CustomException()

        assert_that(
            self.__get_conditional_wait().wait_for(
                func, exceptions_to_ignore=[CustomException]
            ),
            equal_to(False),
            "Custom exception is not ignored",
        )

    def test__wait_for__should_not_raise_exception_when_condition_is_not_satisfied(
        self,
    ):
        def func():
            return False

        assert_that(
            self.__get_conditional_wait().wait_for(func),
            equal_to(False),
            "Condition is satisfied",
        )

    def test__wait_for__should_be_possible_to_wait_for_condition(self):
        def func():
            return True

        assert_that(
            self.__get_conditional_wait().wait_for(func),
            equal_to(True),
            "Condition is not satisfied",
        )

    def test__wait_for_true__should_raise_timeout_error_when_condition_is_not_satisfied(
        self,
    ):
        def func():
            return False

        assert_that(
            calling(self.__get_conditional_wait().wait_for_true).with_args(func),
            raises(TimeoutError),
            "Timeout error is not raised",
        )

    def test__wait_for_true__should_be_possible_to_wait_for_condition(self):
        def func():
            return True

        assert_that(
            calling(self.__get_conditional_wait().wait_for_true).with_args(func),
            is_not(raises(TimeoutError)),
            "Condition is not satisfied",
        )

    def test__wait_for_true__should_be_possible_to_ignore_custom_exception(self):
        raise_exception = {"value": True}

        def func():
            if raise_exception["value"]:
                raise_exception["value"] = False
                raise CustomException()
            return True

        assert_that(
            calling(self.__get_conditional_wait().wait_for_true).with_args(
                func, exceptions_to_ignore=[CustomException]
            ),
            is_not(raises(CustomException)),
            "Custom exception is not ignored",
        )

    def test__wait_for_true__should_raise_not_ignored_exception(self):
        def func():
            raise CustomException()

        assert_that(
            calling(self.__get_conditional_wait().wait_for_true).with_args(func),
            raises(CustomException),
            "Custom exception is not raised",
        )

    def test__wait_for_true__should_be_possible_to_pass_error_message(self):
        part_of_error_message = "test error message"

        def func():
            return False

        assert_that(
            calling(self.__get_conditional_wait().wait_for_true).with_args(
                func, message=part_of_error_message
            ),
            raises(TimeoutError, part_of_error_message),
            "Custom exception is not raised",
        )

    @staticmethod
    def __get_conditional_wait() -> AbstractConditionalWait:
        timeout_configuration = CustomTimeoutConfiguration()
        return ConditionalWait(timeout_configuration)


class CustomException(Exception):
    pass


class CustomTimeoutConfiguration(AbstractTimeoutConfiguration):
    @property
    def implicit(self) -> timedelta:
        return timedelta(seconds=2)

    @property
    def condition(self) -> timedelta:
        return timedelta(seconds=1)

    @property
    def polling_interval(self) -> timedelta:
        return timedelta(milliseconds=250)

    @property
    def command(self) -> timedelta:
        return timedelta(seconds=5)
