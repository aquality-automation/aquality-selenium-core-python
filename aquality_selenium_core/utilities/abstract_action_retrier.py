from abc import ABC, abstractmethod
from typing import List, Type, Callable


class AbstractActionRetrier(ABC):

    @abstractmethod
    def do_with_retry(self, func: Callable, handled_exceptions: List[Type[Exception]]):
        pass
