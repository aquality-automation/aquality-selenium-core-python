import os
from typing import Generator

import pytest

from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.utilities_module import AbstractUtilitiesModule
from tests.test_utilities.test_settings_file.values import TestValues


@pytest.fixture(scope="function")
def get_profile() -> Generator[AbstractSettingsFile, None, None]:
    os.environ["profile"] = "jsontest"
    yield AbstractUtilitiesModule().get_instance_of_settings_file()


@pytest.fixture(scope="function")
def get_default_profile() -> Generator[AbstractSettingsFile, None, None]:
    yield AbstractUtilitiesModule().get_instance_of_settings_file()


@pytest.fixture(scope="function", autouse=True)
def clean_system_variables() -> None:
    __remove_from_environ_if_exist("profile")
    __remove_from_environ_if_exist(TestValues.LANGUAGE_ENV_KEY)
    __remove_from_environ_if_exist(TestValues.TIMEOUT_POLLING_INTERVAL_KEY)
    __remove_from_environ_if_exist(TestValues.ARGUMENTS_ENV_KEY)


def __remove_from_environ_if_exist(key) -> None:
    if key in os.environ:
        del os.environ[key]
