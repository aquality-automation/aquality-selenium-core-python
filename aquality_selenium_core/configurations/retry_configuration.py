"""Module defines retry policy configuration."""
from abc import ABC
from abc import abstractmethod


class AbstractRetryConfiguration(ABC):
    """Describes retry configuration."""

    @property
    @abstractmethod
    def number(self) -> int:
        """Get the number of attempts to retry."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> int:
        """Get the polling interval used in retry."""
        pass
