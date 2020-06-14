from abc import ABC, abstractmethod


class AbcLoggerConfiguration(ABC):

    @abstractmethod
    @property
    def language(self) -> str:
        pass
