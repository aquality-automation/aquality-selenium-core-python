from datetime import timedelta

import pytest
from hamcrest import assert_that
from hamcrest import calling
from hamcrest import equal_to
from hamcrest import is_not
from hamcrest import raises
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException

from aquality_selenium_core.configurations.retry_configuration import (
    AbstractRetryConfiguration,
)
from aquality_selenium_core.utilities.action_retrier import AbstractActionRetrier
from aquality_selenium_core.utilities.action_retrier import ActionRetrier
from aquality_selenium_core.utilities.element_action_retrier import (
    AbstractElementActionRetrier,
)
from aquality_selenium_core.utilities.element_action_retrier import ElementActionRetrier


class TestActionRetries:
    def test__do_with_retry__should_raise_error_if_there_are_no_handled_exceptions(
        self,
    ):
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
            self.__get_action_retrier().do_with_retry(
                func, handled_exceptions=[CustomException]
            ),
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
        retry_configuration = CustomRetryConfiguration()
        return ActionRetrier(retry_configuration)


class TestElementActionRetrier:
    handled_exception_test_data = [
        (StaleElementReferenceException, StaleElementReferenceException()),
        (InvalidElementStateException, InvalidElementStateException()),
    ]

    @pytest.mark.parametrize("exception_type,exception", handled_exception_test_data)
    def test__do_with_retry__should_not_raise_exceptions_handled_by_default(
        self, exception_type, exception
    ):
        raise_exception = {"value": True}

        def func():
            if raise_exception["value"]:
                raise_exception["value"] = False
                raise exception
            return True

        assert_that(
            calling(self.__get_element_action_retrier().do_with_retry).with_args(func),
            is_not(raises(exception_type)),
            "Default exception is not ignored",
        )

    @staticmethod
    def __get_element_action_retrier() -> AbstractElementActionRetrier:
        retry_configuration = CustomRetryConfiguration()
        return ElementActionRetrier(retry_configuration)


class CustomException(Exception):
    pass


class CustomRetryConfiguration(AbstractRetryConfiguration):
    @property
    def number(self) -> int:
        return 2

    @property
    def polling_interval(self) -> timedelta:
        return timedelta(milliseconds=500)
