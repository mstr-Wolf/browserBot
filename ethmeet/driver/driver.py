from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"

class Driver():
    def __init__(self):
        self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)

    def close(self):
        self.__driver.close()

    def __call__(self):
        return self.__driver

    @property
    def _driver(self): return self.__driver

    @_driver.setter
    def _driver(self, driver):
        if WebDriver.__dict__["__module__"] in str(type(driver)):
            self.__driver = driver
        else:
            print("ERROR ****** WEB DRIVER NOT ACCEPTED! ******")
