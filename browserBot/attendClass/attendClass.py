from time import sleep
from sys import exit
from getpass import getpass

from browserBot.clockwork import Clockwork

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
        print(__name__, "started!")
        self.__loginData = None
        self.__login_url = None
        self.__driver = None

        try:
            self.length = float(kwargs["class_length"])
            self.set_meeting_code(meeting_code = kwargs["code"])
        except KeyError: print("ERROR ****** ********\nSome parameters may be missing! Check 'help(AttendClass)' for more details ******")
        except (TypeError, ValueError): print("ERROR ****** ********\n'class_length' parameter may be containing an invalid value! Check 'help(AttendClass)' for more details ******")

    def run(self, login=""):
        self.loginData = login
        print("Process scheduled to", self.get_target().format_datetime(), "\n")
        while True:
            print(self.get_time().format_datetime(), end="\r")
            if self.get_time() >= self.get_target():
                print("Time reached\nStarting process...")
                try:
                    self.driver = "firefox"
                    self.execute()
                    self.shutdownConnection()
                    break
                except selenium.common.exceptions.WebDriverException:
                    print("EXECUTABLE ERROR!\nCheck 'selenium.common.exceptions.WebDriverException' for more informations!\n")
                    print("*"*70)
                    raise selenium.common.exceptions.WebDriverException
            sleep(1)


    def shutdownConnection(self, **kwargs):
        try: self.driver.current_url
        except selenium.common.exceptions.InvalidSessionIdException:
            self.close_drive()

        shutTime = self.length_parser()
        if len(shutTime) == 3:
            self.delay_target(hour = shutTime[0], minute = shutTime[1], second = shutTime[2])
        elif len(shutTime) == 2:
            self.delay_target(hour = shutTime[0], minute = shutTime[1])
        else:
            print("ERROR ****** Length may not be defined. Check AttendClass.length and AttendClass.length_parser for more information!")
            self.close_drive()
            return

        print("Kill scheduled to", self.get_target().format_datetime())
        while True:
            if self.get_time() >= self.get_target():
                self.close_drive()
                break
            sleep(1)
        return

    def execute(self, **kwargs): raise NotImplementedError

    def close_drive(self, **kwargs):
        try: self.driver.close()
        except (AttributeError, selenium.common.exceptions.InvalidSessionIdException):
            print("ERROR ****** Browser driver not implemented or it's already closed! ******")
            exit()

    def doLogin(self): raise NotImplementedError

    def length_parser(self, **kwargs):
        minutes = self.length%60
        if minutes < 0:
            seconds = minutes * 60
            minutes = 0
            hours = int((self.length-minutes)/60)
            return hours, minutes, seconds
        else:
            hours = int((self.length-minutes)/60)
            return hours, minutes

    def set_meeting_code(self, **kwargs): raise NotImplementedError


    @property
    def loginData(self): return self.__loginData

    @loginData.setter
    def loginData(self, user):
        if user == "": user = str(input("User: "))
        else: pass

        passwd = getpass("Password: ")
        self.__loginData = {"user": user, "passwd": passwd}

    @property
    def login_url(self): return self.__login_url

    @login_url.setter
    def login_url(self, url): self.__login_url = url


    @property
    def driver(self): return self.__driver

    @driver.setter
    def driver(self, browser):
        if browser == "firefox": self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)
        else: self.__driver = None

    
