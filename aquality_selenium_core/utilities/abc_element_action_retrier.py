from abc import ABC, abstractmethod
from typing import List, Type

from selenium.common.exceptions import StaleElementReferenceException, InvalidElementStateException

from aquality_selenium_core.utilities.abc_action_retrier import AbcActionRetrier


class AbcElementActionRetrier(AbcActionRetrier, ABC):

    @abstractmethod
    def do_with_retry(self, func, handled_exceptions: List[Type[Exception]]):
        pass

    @staticmethod
    def get_handled_exceptions() -> List[Type[Exception]]:
        return [StaleElementReferenceException, InvalidElementStateException]
