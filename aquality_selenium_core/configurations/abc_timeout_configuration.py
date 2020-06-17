from abc import ABC, abstractmethod

import duration


class AbcTimeoutConfiguration(ABC):
    @property
    @abstractmethod
    def implicit(self) -> duration:
        pass

    @property
    @abstractmethod
    def condition(self) -> duration:
        pass

    @property
    @abstractmethod
    def polling_interval(self) -> duration:
        pass

    @property
    @abstractmethod
    def command(self) -> duration:
        pass
