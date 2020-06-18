from abc import ABC, abstractmethod
from typing import List, Type

from selenium.common.exceptions import StaleElementReferenceException, InvalidElementStateException

from aquality_selenium_core.utilities.abstract_action_retrier import AbstractActionRetrier


class AbstractElementActionRetrier(AbstractActionRetrier, ABC):

    @abstractmethod
    def do_with_retry(self, func, handled_exceptions: List[Type[Exception]]):
        pass

    def get_handled_exceptions(self) -> List[Type[Exception]]:
        return [StaleElementReferenceException, InvalidElementStateException]
