from abc import ABC, abstractmethod

from aquality_selenium_core.configurations.duration import Duration


class AbcRetryConfiguration(ABC):

    @property
    @abstractmethod
    def number(self) -> int:
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> Duration:
        pass
