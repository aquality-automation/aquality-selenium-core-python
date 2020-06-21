from abc import ABC, abstractmethod
from typing import List, Type, Callable, Any, Union


class AbstractActionRetrier(ABC):

    @abstractmethod
    def do_with_retry(self, function_and_args: List[Union[Callable, Any]],
                      handled_exceptions: List[Type[Exception]]) -> Any:
        pass
