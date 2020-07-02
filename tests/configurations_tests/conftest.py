import os
from typing import Generator

import pytest

from aquality_selenium_core.utilities.resource_instance_mock import ResourceInstanceMock
from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile


@pytest.fixture(scope="function")
def get_profile() -> Generator[AbstractSettingsFile, None, None]:
    yield ResourceInstanceMock.get_resource_instance()


def remove_from_environ_if_exist(key) -> None:
    if key in os.environ:
        del os.environ[key]
