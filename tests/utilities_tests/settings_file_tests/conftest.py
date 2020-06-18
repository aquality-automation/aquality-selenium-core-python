import os
from typing import Generator

import pytest

from aquality_selenium_core.utilities.abstract_settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.abstract_utilities_module import AbstractUtilitiesModule
from aquality_selenium_core.utilities.resource_instance_mock import ResourceInstanceMock
from tests.utilities_tests.settings_file_tests.test_keys import TestKeys


@pytest.fixture(scope="function")
def get_test_profile() -> Generator[AbstractSettingsFile, None, None]:
    os.environ["profile"] = 'jsontest'
    yield AbstractUtilitiesModule().get_instance_of_settings_file()


@pytest.fixture(scope="function")
def get_default_profile() -> Generator[AbstractSettingsFile, None, None]:
    yield ResourceInstanceMock.get_resource_instance()


@pytest.fixture(scope="function", autouse=True)
def clean_system_variables() -> None:
    remove_from_environ_if_exist('profile')
    remove_from_environ_if_exist(TestKeys.LANGUAGE_ENV_KEY)
    remove_from_environ_if_exist(TestKeys.TIMEOUT_POLLING_INTERVAL_KEY)
    remove_from_environ_if_exist(TestKeys.ARGUMENTS_ENV_KEY)


def remove_from_environ_if_exist(key) -> None:
    if key in os.environ:
        del os.environ[key]
