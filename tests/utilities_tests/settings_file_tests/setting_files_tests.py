import os
from distutils.util import strtobool
from typing import List

import pytest
from hamcrest import assert_that
from hamcrest import calling
from hamcrest import equal_to
from hamcrest import raises

from aquality_selenium_core.exceptions.illegal_argument_exception import (
    IllegalArgumentException,
)
from aquality_selenium_core.utilities.abstract_settings_file import AbstractSettingsFile
from tests.utilities_tests.settings_file_tests.test_keys import TestKeys


class TestsSettingsFiles:
    def test_should_be_possible_to_override_boolean_value_via_environment_variable(
        self, get_test_profile
    ):
        old_value: bool = get_test_profile.get_value(TestKeys.BOOLEANVALUE_ENV_KEY)
        target_value: bool = not old_value
        os.environ[TestKeys.BOOLEANVALUE_ENV_KEY] = str(target_value)
        assert_that(
            bool(strtobool(get_test_profile.get_value(TestKeys.BOOLEANVALUE_ENV_KEY))),
            equal_to(target_value),
            "value passed via env var is not used by SettingsFile",
        )

    def test_should_be_possible_to_set_value_which_is_absent_in_json_file(
        self, get_test_profile
    ):
        assert_that(
            not get_test_profile.is_value_present(TestKeys.ABSENTVALUE_PATH),
            "value should be absent by default",
        )
        target_value: str = str(True)
        os.environ[TestKeys.ABSENTVALUE_PATH] = target_value
        assert_that(
            get_test_profile.is_value_present(TestKeys.ABSENTVALUE_PATH),
            "value should be present after set",
        )
        assert_that(
            get_test_profile.get_value(TestKeys.ABSENTVALUE_PATH),
            equal_to(target_value),
            "value passed via env var is not used by SettingsFile",
        )

    def test_should_be_possible_to_get_default_content(self, get_default_profile):
        language: str = get_default_profile.get_value("logger.language")
        assert_that(
            language,
            equal_to("en"),
            "Logger language in default settings file should be read correctly",
        )

    def test_should_be_possible_to_get_value(self, get_test_profile):
        language_path = "logger.language"
        language_key = "language"

        language: str = get_test_profile.get_value(language_path)
        assert_that(
            language,
            equal_to(TestKeys.EXPECTED_LANGUAGES[language_key]),
            f"Logger language in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        new_lang: str = "newLang"
        os.environ[TestKeys.LANGUAGE_ENV_KEY] = new_lang

        language = get_test_profile.get_value(language_path)
        assert_that(
            language,
            equal_to(new_lang),
            f"Logger language in settings file {TestKeys.FILE_NAME} "
            f"should be overridden with environment variable",
        )

    def test_should_be_possible_to_get_list_of_values(self, get_test_profile):
        arguments_path: str = "arguments.start"
        expected_arguments: List[str] = ["first", "second"]
        arguments: List[str] = get_test_profile.get_list(arguments_path)

        assert_that(arguments is not None)
        assert_that(
            arguments,
            equal_to(expected_arguments),
            f"List of values in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        expected_arguments = ["firstNew", "secondNew"]
        new_args: str = "firstNew,secondNew"
        os.environ[TestKeys.ARGUMENTS_ENV_KEY] = new_args
        arguments = get_test_profile.get_list(arguments_path)
        assert_that(arguments is not None)
        assert_that(
            arguments,
            equal_to(expected_arguments),
            f"Value in list in settings file {TestKeys.FILE_NAME} be overridden with environment variable",
        )

    def test_should_be_possible_to_get_map(self, get_test_profile):
        logger_path: str = "logger"

        languages = get_test_profile.get_dictionary(logger_path)

        assert_that(languages is not None)
        assert_that(
            languages,
            equal_to(TestKeys.EXPECTED_LANGUAGES),
            f"Dictionary of values in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        new_language_value = "newLangMap"
        expected_languages = {"language": new_language_value}
        os.environ[TestKeys.LANGUAGE_ENV_KEY] = new_language_value
        languages = get_test_profile.get_dictionary(logger_path)

        assert_that(languages is not None)
        assert_that(
            languages,
            equal_to(expected_languages),
            f"Dictionary of values in settings file {TestKeys.FILE_NAME} "
            f"should be overridden with environment variable",
        )

    def test_should_be_possible_to_check_is_value_present(self, get_test_profile):
        is_time_out_present: bool = get_test_profile.is_value_present(
            TestKeys.TIMEOUT_POLLING_INTERVAL_PATH
        )

        assert_that(
            is_time_out_present,
            f"{TestKeys.TIMEOUT_POLLING_INTERVAL_PATH} value should be present in settings file {TestKeys.FILE_NAME}",
        )

        wrong_path: str = "blabla"
        is_wrong_path_present: bool = get_test_profile.is_value_present(wrong_path)
        assert_that(
            not is_wrong_path_present,
            f"{wrong_path} value should not be present in settings file {TestKeys.FILE_NAME}",
        )

    def test_should_be_possible_to_check_that_null_value_is_present(
        self, get_test_profile
    ):
        is_null_value_present = get_test_profile.is_value_present(
            TestKeys.NULLVALUE_PATH
        )
        assert_that(
            is_null_value_present,
            f"{TestKeys.NULLVALUE_PATH} value should be present in settings file {TestKeys.FILE_NAME}",
        )

    methods_to_check = [
        AbstractSettingsFile.get_list,
        AbstractSettingsFile.get_dictionary,
        AbstractSettingsFile.get_value,
    ]

    @pytest.mark.parametrize("func", methods_to_check)
    def test_should_throw_exception_when_value_not_found(self, func, get_test_profile):
        wrong_path: str = "blabla"
        assert_that(
            calling(getattr(get_test_profile, func.__name__)).with_args(wrong_path),
            raises(IllegalArgumentException),
        )
