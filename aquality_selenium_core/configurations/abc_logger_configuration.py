from abc import ABC, abstractmethod


class AbcLoggerConfiguration(ABC):

    @property
    @abstractmethod
    def language(self) -> str:
        pass
