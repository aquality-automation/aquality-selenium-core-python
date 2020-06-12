from abc import ABC, abstractmethod
from typing import List, Type


class AbcActionRetrier(ABC):

    @abstractmethod
    def do_with_retry(self, func, handled_exceptions: List[Type[Exception]]):
        pass
