from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Type


class AbcActionRetrier(ABC):
    @abstractmethod
    def do_with_retry(self, func, handled_exceptions: List[Type[Exception]]):
        pass
