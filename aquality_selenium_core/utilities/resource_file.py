# -*- coding: utf-8 -*-
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ResourceFile:

    @staticmethod
    def get_resource_path(resource_name: str) -> str:
        return os.path.join(ROOT_DIR, 'resources', resource_name)
