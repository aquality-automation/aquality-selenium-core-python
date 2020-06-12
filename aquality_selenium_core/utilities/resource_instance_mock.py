from aquality_selenium_core.utilities.abc_utilities_module import AbcUtilitiesModule


class ResourceInstanceMock:
    @staticmethod
    def get_resource_instance():
        return AbcUtilitiesModule().get_instance_of_settings_file()
