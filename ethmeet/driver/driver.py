from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"

class Driver():
    def __init__(self, auto_start = True):
        if ["auto_start"] == False:
            self.__driver = None
        else:
            self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)

    def __start(self):
        self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)

    @property
    def driver(self): return self.__driver

    @driver.setter
    def driver(self, driver):
        if WebDriver.__dict__["__module__"] in str(type(driver)):
            self.__driver = driver
        else:
            print("ERROR ****** WEB DRIVER NOT ACCEPTED! ******")
