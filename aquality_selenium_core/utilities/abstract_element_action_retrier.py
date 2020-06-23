from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Callable
from typing import List
from typing import Type
from typing import Union

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import StaleElementReferenceException

from aquality_selenium_core.utilities.abstract_action_retrier import (
    AbstractActionRetrier,
)


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):
    @abstractmethod
    def do_with_retry(
        self,
        function_and_args: List[Union[Callable, Any]],
        handled_exceptions: List[Type[Exception]],
    ) -> Any:
        pass

    def get_handled_exceptions(self) -> List[Type[Exception]]:
        return [StaleElementReferenceException, InvalidElementStateException]
