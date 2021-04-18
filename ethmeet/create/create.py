from abc import ABC, abstractmethod
from time import sleep

import selenium.common.exceptions

from ..driver import Driver


class Create(ABC, Driver):
    def __init__(self, **kwargs):
        super(ABC).__init__()
        self.__code = None

        try:
            self._driver = kwargs["driver"]
        except (KeyError): pass

    @abstractmethod
    def new_meet(self):
        return

    def _set_new_meet(self, code):
        self.__code = code

    @property
    def code(self):
        try:
            return self.__code
        except AttributeError:
            print("Code unset!")
            return None

class CreateGoogle(Create):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def new_meet(self):
        try:
            self._driver.get("https://meet.google.com/")
        except AttributeError:
            print("ERROR ****** WEB DIVER OR LOGIN URL UNSET! ******")
            raise

        try:
            button = self._driver.find_element_by_class_name("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe cjtUbb Dg7t5c".replace(" ", "."))
            button.click()
            button = self._driver.find_element_by_class_name("VfPpkd-StrnGf-rymPhb-ibnC6b VfPpkd-rymPhb-ibnC6b-OWXEXe-tPcied-hXIJHe".replace(" ", "."))
            button.click()
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("ERROR ****** Login failed. No element found! Couldn't stablish connection ******")
            return False

        for _ in range(5):
            try:
                self._set_new_meet(self._driver.find_element_by_class_name("Hayy8b").text)
                break
            except (selenium.common.exceptions.NoSuchElementException): sleep(1)

        self._driver.get("https://meet.google.com/")
        return True
