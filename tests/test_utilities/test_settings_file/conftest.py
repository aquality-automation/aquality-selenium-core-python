import os
from typing import Generator

import pytest

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.settings_file import JsonSettingsFile
from tests.test_utilities.test_settings_file.values import TestValues

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="function")
def get_profile() -> Generator[AbstractSettingsFile, None, None]:
    os.environ["profile"] = "jsontest"
    yield __get_json_settings_file()


@pytest.fixture(scope="function")
def get_default_profile() -> Generator[AbstractSettingsFile, None, None]:
    yield __get_json_settings_file()


@pytest.fixture(scope="function", autouse=True)
def clean_system_variables() -> None:
    __remove_from_environ_if_exist("profile")
    __remove_from_environ_if_exist(TestValues.LANGUAGE_ENV_KEY)
    __remove_from_environ_if_exist(TestValues.TIMEOUT_POLLING_INTERVAL_KEY)
    __remove_from_environ_if_exist(TestValues.ARGUMENTS_ENV_KEY)


def __remove_from_environ_if_exist(key) -> None:
    if key in os.environ:
        del os.environ[key]


def __get_json_settings_file() -> AbstractSettingsFile:
    os_var_profile = os.environ.get("profile")
    settings_file_name = (
        f"settings.{os_var_profile}.json" if os_var_profile else "settings.json"
    )
    return JsonSettingsFile(settings_file_name, ROOT_DIR)
