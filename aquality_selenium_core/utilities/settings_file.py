from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List


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

    def get_value_or_default(self, path: str, default_value: object) -> Any:
        return self.get_value(path) if self.is_value_present(path) else default_value
