"""Module defines abstraction for element cache configuration."""
from abc import ABC
from abc import abstractmethod


class AbstractElementCacheConfiguration(ABC):
    """Provides element's cache configuration."""

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        """Is element caching allowed or not."""
        pass
