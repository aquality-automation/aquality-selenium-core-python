"""Module defines timeouts configuration."""
from abc import ABC
from abc import abstractmethod
from datetime import timedelta


class AbstractTimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""

    @property
    @abstractmethod
    def implicit(self) -> timedelta:
        """Get WedDriver ImplicitWait timeout."""
        pass

    @property
    @abstractmethod
    def condition(self) -> timedelta:
        """Get default ConditionalWait timeout."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> timedelta:
        """Get ConditionalWait polling interval."""
        pass

    @property
    @abstractmethod
    def command(self) -> timedelta:
        """Get WebDriver Command timeout."""
        pass
