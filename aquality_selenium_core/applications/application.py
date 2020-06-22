# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from datetime import timedelta

from selenium.webdriver import Remote


class AbstractApplication(ABC):
    """
    Interface of any application controlled by Selenium WebDriver API.
    """

    @property
    @abstractmethod
    def driver(self) -> Remote:
        """
        :return: Current instance of driver.
        """
        pass

    @abstractmethod
    def is_started(self) -> bool:
        """
        :return: Is the application already running or not.
        """
        pass

    @abstractmethod
    def set_implicit_wait_timeout(self, value: timedelta) -> None:
        """
        Sets implicit wait timeout to Selenium WebDriver.
        :param value: timeout value to set.
        """
        pass
