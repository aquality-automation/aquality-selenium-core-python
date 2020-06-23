"""Module for simulation calling resources for library source code."""
from aquality_selenium_core.utilities.utilities_module import AbstractUtilitiesModule


class ResourceInstanceMock:
    """Class for simulation calling resources for library source code."""

    @staticmethod
    def get_resource_instance():
        """
        Get instance of settings file for library source code.

        :return: Instance of settings file.
        """
        return AbstractUtilitiesModule().get_instance_of_settings_file()
