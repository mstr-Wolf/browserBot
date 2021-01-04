import sys
from datetime import timedelta
from time import sleep
from getpass import getpass

from clockwork import Clockwork
from attendClass.utils import assert_meeting_code

import selenium.common.exceptions
from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"



class AttendClass(Clockwork):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'hour' (int): Class' start hour\n
            'minute' (int): Class' start minute\n
        """

        super().__init__(**kwargs)
        self.driver = None
        try:
            self.MEET_URL = assert_meeting_code(kwargs["code"], 10, 12)
            self.length = float(kwargs["class_length"])
        except KeyError:
            print("ERROR\n********\nSome parameters may be missing! Check 'help(AttendClass)' for more details")
        except (TypeError, ValueError):
            print("ERROR\n********\n'class_length' parameter may be containing an invalid value! Check 'help(AttendClass)' for more details")

    def run(self):
        print(__name__, "started!")
        print("Process scheduled to", self._Clockwork__target.format_datetime(), "\n")
        while True:
            print(self.get_time().format_datetime(), end="\r")
            if self._Clockwork__time_now == self._Clockwork__target or self._Clockwork__time_now > self._Clockwork__target:
                print("Time reached\nStarting process...")
                try:
                    self.execute()
                    sys.exit(0)
                except selenium.common.exceptions.WebDriverException:
                    print("EXECUTABLE ERROR!\nCheck 'selenium.common.exceptions.WebDriverException' for more informations!\n")
                    print("*"*70)
                    raise selenium.common.exceptions.WebDriverException
            sleep(1)

    def execute(self, **kwargs):
        self.driver = WebDriver(executable_path=EXECUTABLE_PATH)
        self.driver.get(self.MEET_URL)

        shutTime = self.get_class_duration()
        self.shutdownConnection(hours = shutTime[0], minutes = shutTime[1])
        return

    def shutdownConnection(self, **kwargs):
        self._Clockwork__target = self.get_time() + timedelta(hours=kwargs["hours"], minutes=kwargs["minutes"])
        print("Kill scheduled to", self._Clockwork__target.format_datetime())
        while True:
            if self.get_time() == self._Clockwork__target or self.get_time() > self._Clockwork__target:
                self.driver.close()
                break
            sleep(1)
        return

    def get_class_duration(self, **kwargs):
        minutes = self.length%60
        hours = int((self.length-minutes)/60)
        return hours, minutes



class AutomaticLogin(AttendClass):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'hour' (int): Class' start hour\n
            'minute' (int): Class' start minute\n
        """
        super().__init__(**kwargs)
        self.login_url = "https://accounts.google.com/Login?hl=pt-BR"
        self.loginData = self.getLoginData()

    def execute(self, **kwargs):
        start_time = self._Clockwork__time_now

        self.driver = WebDriver(executable_path=EXECUTABLE_PATH)
        self.doLogin()
        self.driver.get(self.MEET_URL)

        print("Login time: ", self.get_time() - start_time)
        shutTime = self.get_class_duration()
        self.shutdownConnection(hours = shutTime[0], minutes = shutTime[1])
        return

    def getLoginData(self):
        user = str(input("Meet's user: "))
        passwd = getpass("Password: ")
        return {"user": user, "passwd": passwd}

    def doLogin(self):
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("identifierId").send_keys(self.loginData["user"])
        self.driver.find_element_by_id("identifierNext").click()

        try:
            self.driver.find_element_by_name("password").send_keys(self.loginData["passwd"])
        except selenium.common.exceptions.NoSuchElementException:
            sleep(6)
            self.driver.find_element_by_name("password").send_keys(self.loginData["passwd"])
        self.driver.find_element_by_id("passwordNext").click()
