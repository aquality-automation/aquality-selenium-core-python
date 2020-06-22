"""Utilities for operations with resource files."""
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ResourceFile:
    """Util class for operation with resource files."""

    @staticmethod
    def get_resource_path(resource_name: str) -> str:
        """Get path to resource file by specified path."""
        return os.path.join(ROOT_DIR, "resources", resource_name)
