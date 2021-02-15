from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"

class Driver():
    def __init__(self):
        self.__driver = None

    @property
    def driver(self): return self.__driver

    @driver.setter
    def driver(self, browser):
        if browser == "firefox": self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)
        else: self.__driver = None
