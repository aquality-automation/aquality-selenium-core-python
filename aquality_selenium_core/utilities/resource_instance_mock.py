from aquality_selenium_core.utilities.abstract_utilities_module import (
    AbstractUtilitiesModule,
)


class ResourceInstanceMock:
    @staticmethod
    def get_resource_instance():
        return AbstractUtilitiesModule().get_instance_of_settings_file()
