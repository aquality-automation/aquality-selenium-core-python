import os
from distutils.util import strtobool

import pytest
from hamcrest import assert_that
from hamcrest import calling
from hamcrest import equal_to
from hamcrest import not_none
from hamcrest import raises

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile
from tests.test_utilities.test_settings_file.keys import TestKeys


class TestSettingsFiles:
    def test_should_be_possible_to_override_boolean_value_via_environment_variable(
        self, get_profile
    ):
        key = "booleanValue"
        old_value = get_profile.get_value(key)
        target_value = not old_value
        os.environ[key] = str(target_value)
        assert_that(
            bool(strtobool(get_profile.get_value(key))),
            equal_to(target_value),
            "value passed via env var is not used by SettingsFile",
        )

    def test_should_be_possible_to_set_value_which_is_absent_in_json_file(
        self, get_profile
    ):
        assert_that(
            get_profile.is_value_present(TestKeys.ABSENTVALUE_PATH),
            equal_to(False),
            "value should be absent by default",
        )
        target_value = str(True)
        os.environ[TestKeys.ABSENTVALUE_PATH] = target_value
        assert_that(
            get_profile.is_value_present(TestKeys.ABSENTVALUE_PATH),
            equal_to(True),
            "value should be present after set",
        )
        assert_that(
            get_profile.get_value(TestKeys.ABSENTVALUE_PATH),
            equal_to(target_value),
            "value passed via env var is not used by SettingsFile",
        )

    def test_should_be_possible_to_get_default_content(self, get_default_profile):
        language = get_default_profile.get_value("logger.language")
        assert_that(
            language,
            equal_to("en"),
            "Logger language in default settings file should be read correctly",
        )

    def test_should_be_possible_to_get_value(self, get_profile):
        language_path = "logger.language"
        language_key = "language"

        language = get_profile.get_value(language_path)
        assert_that(
            language,
            equal_to(TestKeys.EXPECTED_LANGUAGES[language_key]),
            f"Logger language in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        new_lang = "newLang"
        os.environ[language_path] = new_lang

        language = get_profile.get_value(language_path)
        assert_that(
            language,
            equal_to(new_lang),
            f"Logger language in settings file {TestKeys.FILE_NAME} "
            f"should be overridden with environment variable",
        )

    def test_should_be_possible_to_get_list_of_values(self, get_profile):
        arguments_path = "arguments.start"
        expected_arguments = ["first", "second"]
        arguments = get_profile.get_list(arguments_path)

        assert_that(arguments, not_none(), "Arguments list is none")
        assert_that(
            arguments,
            equal_to(expected_arguments),
            f"List of values in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        expected_arguments = ["firstNew", "secondNew"]
        new_args = "firstNew,secondNew"
        os.environ[TestKeys.ARGUMENTS_ENV_KEY] = new_args
        arguments = get_profile.get_list(arguments_path)
        assert_that(arguments, not_none(), "Arguments list is none")
        assert_that(
            arguments,
            equal_to(expected_arguments),
            f"Value in list in settings file {TestKeys.FILE_NAME} be overridden with environment variable",
        )

    def test_should_be_possible_to_get_map(self, get_profile):
        logger_path = "logger"

        languages = get_profile.get_dictionary(logger_path)

        assert_that(languages, not_none(), "Languages list is none")

        assert_that(
            languages,
            equal_to(TestKeys.EXPECTED_LANGUAGES),
            f"Dictionary of values in settings file {TestKeys.FILE_NAME} should be read correctly",
        )

        new_language_value = "newLangMap"
        expected_languages = {"language": new_language_value}
        os.environ[TestKeys.LANGUAGE_ENV_KEY] = new_language_value
        languages = get_profile.get_dictionary(logger_path)

        assert_that(languages, not_none(), "Languages list is none")

        assert_that(
            languages,
            equal_to(expected_languages),
            f"Dictionary of values in settings file {TestKeys.FILE_NAME} "
            f"should be overridden with environment variable",
        )

    def test_should_be_possible_to_check_is_value_present(self, get_profile):
        key = "timeouts.timeoutPollingInterval"
        is_time_out_present = get_profile.is_value_present(key)

        assert_that(
            is_time_out_present,
            f"{key} value should be present in settings file {TestKeys.FILE_NAME}",
        )

        wrong_path = "blabla"
        is_wrong_path_present = get_profile.is_value_present(wrong_path)
        assert_that(
            is_wrong_path_present,
            equal_to(False),
            f"{wrong_path} value should not be present in settings file {TestKeys.FILE_NAME}",
        )

    def test_should_be_possible_to_check_that_null_value_is_present(self, get_profile):
        key = "nullValue"
        is_null_value_present = get_profile.is_value_present(key)
        assert_that(
            is_null_value_present,
            equal_to(True),
            f"{key} value should be present in settings file {key}",
        )

    @pytest.mark.parametrize(
        "func",
        [
            AbstractSettingsFile.get_list,
            AbstractSettingsFile.get_dictionary,
            AbstractSettingsFile.get_value,
        ],
    )
    def test_should_throw_exception_when_value_not_found(self, func, get_profile):
        wrong_path = "blabla"
        assert_that(
            calling(getattr(get_profile, func.__name__)).with_args(wrong_path),
            raises(ValueError),
        )
