from abc import ABC, abstractmethod


class AbcElementCacheConfiguration(ABC):

    @property
    @abstractmethod
    def enabled(self) -> bool:
        pass
