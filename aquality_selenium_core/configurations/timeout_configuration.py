"""Module defines timeouts configuration."""
from abc import ABC
from abc import abstractmethod


class AbstractTimeoutConfiguration(ABC):
    """Abstraction for timeout configuration."""

    @property
    @abstractmethod
    def implicit(self) -> int:
        """Get WedDriver ImplicitWait timeout."""
        pass

    @property
    @abstractmethod
    def condition(self) -> int:
        """Get default ConditionalWait timeout."""
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> int:
        """Get ConditionalWait polling interval."""
        pass

    @property
    @abstractmethod
    def command(self) -> int:
        """Get WebDriver Command timeout."""
        pass
