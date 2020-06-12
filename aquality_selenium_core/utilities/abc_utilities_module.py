import os
import sys
from typing import Callable

import rootpath

from aquality_selenium_core.utilities.abc_action_retrier import AbcActionRetrier
from aquality_selenium_core.utilities.abc_element_action_retrier import AbcElementActionRetrier
from aquality_selenium_core.utilities.abc_settings_file import AbcSettingsFile
from aquality_selenium_core.utilities.json_setting_file import JsonSettingsFile


class AbcUtilitiesModule:

    def get_action_retrier_implementation(self) -> Callable:
        return AbcActionRetrier

    def get_element_action_retrier_implementation(self) -> Callable:
        return AbcElementActionRetrier

    def get_instance_of_settings_file(self) -> AbcSettingsFile:
        frame = sys._getframe(1).f_globals['__package__']
        os_var_profile = os.environ.get('profile')
        settings_file_name = f'settings.{os_var_profile}.json' if os_var_profile else 'settings.json'
        path_to_file = os.path.join(rootpath.detect(), frame.split(".")[0], 'resources', settings_file_name)
        return JsonSettingsFile(path_to_file)
