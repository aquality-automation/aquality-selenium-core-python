from abc import ABC, abstractmethod


class AbcElementCacheConfiguration(ABC):

    @abstractmethod
    @property
    def enabled(self) -> bool:
        pass
