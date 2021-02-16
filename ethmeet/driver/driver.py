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

    @driver.setter
    def driver(self, driver):
        if WebDriver.__dict__["__module__"] in str(type(driver)):
            self.__driver = driver
        else:
            print("ERROR ****** WEB DRIVER NOT ACCEPTED! ******")
