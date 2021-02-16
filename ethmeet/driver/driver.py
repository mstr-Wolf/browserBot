from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"

class Driver():
    def __init__(self, **kwargs):
        self.__driver = None
        try:
            if kwargs["auto_start"] == True:
                self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)
            else: pass
        except KeyError: pass

    def start(self):
        self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)

    @property
    def driver(self): return self.__driver
