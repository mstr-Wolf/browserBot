from abc import ABC, abstractmethod
from time import sleep

import selenium.common.exceptions

class CreateMeet(ABC):
    def __init__(self, driver = None,**kwargs):
        self.__code = None
        self.__driver = driver

    @abstractmethod
    def new_class(self):
        return

    def set_new_class(self, code):
        self.__code = code

    @property
    def code(self):
        try:
            return self.__code
        except AttributeError:
            print("Code unset!")
            return None

    @property
    def driver(self): return self.__driver

class CreateGoogle(CreateMeet):
    def __init__(self, driver = None, **kwargs):
        super().__init__(driver, **kwargs)

    def new_class(self):
        self.driver.get("https://meet.google.com/")
        button = self.driver.find_element_by_class_name("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe cjtUbb Dg7t5c".replace(" ", "."))
        button.click()
        button = self.driver.find_element_by_class_name("VfPpkd-rymPhb-ibnC6b VfPpkd-rOvkhd-rymPhb-ibnC6b-OWXEXe-tPcied-hXIJHe".replace(" ", "."))
        button.click()

        for _ in range(5):
            try:
                self.set_new_class(self.driver.find_element_by_class_name("Hayy8b").text)
                break
            except (selenium.common.exceptions.NoSuchElementException): sleep(1)

        self.driver.get("https://meet.google.com/")
