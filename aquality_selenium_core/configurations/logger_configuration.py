"""Module defines logger configuration."""
from abc import ABC
from abc import abstractmethod


class AbstractLoggerConfiguration(ABC):
    """Describes logger configuration."""

    @property
    @abstractmethod
    def language(self) -> str:
        """Get language of framework."""
        pass

    @property
    @abstractmethod
    def log_page_source(self) -> bool:
        """Perform page source logging in case of catastrophic failures or not."""
        pass
