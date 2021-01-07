from time import sleep
from sys import exit
from getpass import getpass

from clockwork import Clockwork

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
        self.driver = None
        self.login_url = ""

        try:
            self.length = float(kwargs["class_length"])
            self.set_meeting_code(meeting_code = kwargs["code"])
        except KeyError: print("ERROR ****** ********\nSome parameters may be missing! Check 'help(AttendClass)' for more details ******")
        except (TypeError, ValueError): print("ERROR ****** ********\n'class_length' parameter may be containing an invalid value! Check 'help(AttendClass)' for more details ******")

        self.getLoginData()

    def run(self):
        print("Process scheduled to", self.get_target().format_datetime(), "\n")
        while True:
            print(self.get_time().format_datetime(), end="\r")
            if self.get_time() >= self.get_target():
                print("Time reached\nStarting process...")
                try:
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

        shutTime = self.get_class_length()
        if len(shutTime) == 3:
            self.delay_target(hour = shutTime[0], minute = shutTime[1], second = shutTime[2])
        elif len(shutTime) == 2:
            self.delay_target(hour = shutTime[0], minute = shutTime[1])
        else:
            print("ERROR ****** Length may not be defined. Check AttendClass.length and AttendClass.get_class_length for more information!")
            self.close_drive()
            return

        print("Kill scheduled to", self.get_target().format_datetime())
        while True:
            if self.get_time() >= self.get_target():
                self.close_drive()
                break
            sleep(1)
        return

    def get_class_length(self, **kwargs):
        minutes = self.length%60
        if minutes < 0:
            seconds = minutes * 60
            minutes = 0
            hours = int((self.length-minutes)/60)
            return hours, minutes, seconds
        else:
            hours = int((self.length-minutes)/60)
            return hours, minutes

    def getLoginData(self):
        user = str(input("User: "))
        passwd = getpass("Password: ")
        self.loginData = {"user": user, "passwd": passwd}

    def execute(self, **kwargs): raise NotImplementedError

    def close_drive(self, **kwargs):
        try: self.driver.close()
        except (AttributeError, selenium.common.exceptions.InvalidSessionIdException):
            print("ERROR ****** Browser driver not implemented or it's already closed! ******")
            exit()

    def doLogin(self): raise NotImplementedError

    def set_meeting_code(self, **kwargs): raise NotImplementedError



class GoogleClass(AttendClass):
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

    def execute(self, **kwargs):
        self.driver = WebDriver(executable_path=EXECUTABLE_PATH)
        self.doLogin()

        try: self.driver.get(self.MEET_URL)
        except selenium.common.exceptions.InvalidArgumentException:
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            self.close_drive()
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        return

    def doLogin(self):
        start_time = self.get_time()
        self.driver.get(self.login_url)

        self.driver.find_element_by_id("identifierId").send_keys(self.loginData["user"])
        self.driver.find_element_by_id("identifierNext").click()

        for _ in range(15):
            try:
                self.driver.find_element_by_name("password").send_keys(self.loginData["passwd"])
                break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException):
                sleep(1)

        try:
            self.driver.find_element_by_id("passwordNext").click()
            try:
                if self.driver.find_element_by_class_name("EjBTad"):
                    print("ERROR ****** Login failed. Check your password and try again! ******")
                    self.close_drive()
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
                print("ERROR ****** Login failed. Check your connection and try again! ******")
                self.close_drive()
                return
        print("Login time: ", self.get_time() - start_time)

    def set_meeting_code(self, **kwargs):
        try:
            kwargs["meeting_code"] + "STRING_TEST"
        except TypeError:
            print("ERROR ****** Meeting code must be string! ******")
            self.MEET_URL =  ""
            return

        code_len = len(kwargs["meeting_code"])
        if code_len != 12 and code_len != 10:
            print("ERROR ****** Meeting code not accepted! Please check again ******")
            self.MEET_URL =  ""
        elif (code_len == 12 and kwargs["meeting_code"][3] == "-" and kwargs["meeting_code"][8] == "-") or code_len == 10:
            for crc in kwargs["meeting_code"]:
                try:
                    int(crc)
                    print("ERROR ****** Meeting code must not contain numbers! ******")
                    self.MEET_URL =  ""
                    return
                except ValueError: continue
            self.MEET_URL="https://meet.google.com/%s" % kwargs["meeting_code"]



class ZoomClass(GoogleClass):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'hour' (int): Class' start hour\n
            'minute' (int): Class' start minute\n
        """
        super().__init__(**kwargs)
        self.login_url = "https://zoom.us/google_oauth_signin"

    def execute(self, **kwargs):
        self.driver = WebDriver(executable_path=EXECUTABLE_PATH)
        self.doLogin()

        try:
            self.driver.get(self.MEET_URL)
            self.driver.find_elements_by_tag_name("a")[4].click()
        except (selenium.common.exceptions.InvalidArgumentException, selenium.common.exceptions.NoSuchElementException):
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            self.close_drive()
            return
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        self.driver.find_element_by_id("joinBtn").click()
        return

    def set_meeting_code(self, **kwargs):
        if "https://zoom.us/j/" in kwargs["meeting_code"]:
            self.MEET_URL = kwargs["meeting_code"]
        else: self.MEET_URL="https://zoom.us/j/%s" % kwargs["meeting_code"]
