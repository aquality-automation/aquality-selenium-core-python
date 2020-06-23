"""Module provides implementations for utilities module."""
import os
import sys
from typing import Callable

import rootpath

from aquality_selenium_core.utilities.action_retrier import AbstractActionRetrier
from aquality_selenium_core.utilities.action_retrier import AbstractElementActionRetrier
from aquality_selenium_core.utilities.settings_file import AbstractSettingsFile
from aquality_selenium_core.utilities.settings_file import JsonSettingsFile


class AbstractUtilitiesModule:
    """Class provides implementations for utilities module."""

    def get_action_retrier_implementation(self) -> Callable:
        """
        Provide implementation of ActionRetrier.

        :return: Implementation of ActionRetrier.
        """
        return AbstractActionRetrier

    def get_element_action_retrier_implementation(self) -> Callable:
        """
        Return implementation of AbstractElementActionRetrier.

        :return: Implementation of AbstractElementActionRetrier.
        """
        return AbstractElementActionRetrier

    def get_instance_of_settings_file(self) -> AbstractSettingsFile:
        """
        Return implementation of AbstractSettingsFile.

        :return: Implementation of AbstractSettingsFile.
        """
        frame = sys._getframe(1).f_globals["__package__"]
        os_var_profile = os.environ.get("profile")
        settings_file_name = (
            f"settings.{os_var_profile}.json" if os_var_profile else "settings.json"
        )
        path_to_file = os.path.join(
            rootpath.detect(), frame.split(".")[0], "resources", settings_file_name
        )
        return JsonSettingsFile(path_to_file)
