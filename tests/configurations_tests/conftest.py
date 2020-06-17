import os
from typing import Generator

import pytest

from aquality_selenium_core.utilities.abc_settings_file import AbcSettingsFile
from aquality_selenium_core.utilities.resource_instance_mock import ResourceInstanceMock


@pytest.fixture(scope="function")
def get_profile() -> Generator[AbcSettingsFile, None, None]:
    yield ResourceInstanceMock.get_resource_instance()


def remove_from_environ_if_exist(key) -> None:
    if key in os.environ:
        del os.environ[key]
