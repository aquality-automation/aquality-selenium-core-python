from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AbstractSettingsFile(ABC):

    @abstractmethod
    def get_value(self, path: str) -> Any:
        pass

    @abstractmethod
    def get_list(self, path: str) -> List[str]:
        pass

    @abstractmethod
    def get_dictionary(self, path: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def is_value_present(self, path: str) -> bool:
        pass

    def get_value_or_default(self, path: str, default_value: object) -> str:
        return self.get_value(path) if self.is_value_present(path) else default_value
