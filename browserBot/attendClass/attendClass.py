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

        try:
            self.length = float(kwargs["class_length"])
            self.set_meeting_code(meeting_code = kwargs["code"])
        except KeyError: print("ERROR ****** ********\nSome parameters may be missing! Check 'help(AttendClass)' for more details ******")
        except (TypeError, ValueError): print("ERROR ****** ********\n'class_length' parameter may be containing an invalid value! Check 'help(AttendClass)' for more details ******")

        self.setLoginData()

    def run(self):
        print("Process scheduled to", self.get_target().format_datetime(), "\n")
        while True:
            print(self.get_time().format_datetime(), end="\r")
            if self.get_time() >= self.get_target():
                print("Time reached\nStarting process...")
                try:
                    self.set_driver()
                    self.execute()
                    self.shutdownConnection()
                    break
                except selenium.common.exceptions.WebDriverException:
                    print("EXECUTABLE ERROR!\nCheck 'selenium.common.exceptions.WebDriverException' for more informations!\n")
                    print("*"*70)
                    raise selenium.common.exceptions.WebDriverException
            sleep(1)

    def shutdownConnection(self, **kwargs):
        try: self.get_driver.current_url
        except selenium.common.exceptions.InvalidSessionIdException:
            self.close_drive()

        shutTime = self.set_class_length()
        if len(shutTime) == 3:
            self.delay_target(hour = shutTime[0], minute = shutTime[1], second = shutTime[2])
        elif len(shutTime) == 2:
            self.delay_target(hour = shutTime[0], minute = shutTime[1])
        else:
            print("ERROR ****** Length may not be defined. Check AttendClass.length and AttendClass.set_class_length for more information!")
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
        try: self.get_driver.close()
        except (AttributeError, selenium.common.exceptions.InvalidSessionIdException):
            print("ERROR ****** Browser driver not implemented or it's already closed! ******")
            exit()

    def doLogin(self): raise NotImplementedError

    def set_class_length(self, **kwargs):
        minutes = self.length%60
        if minutes < 0:
            seconds = minutes * 60
            minutes = 0
            hours = int((self.length-minutes)/60)
            return hours, minutes, seconds
        else:
            hours = int((self.length-minutes)/60)
            return hours, minutes

    def setLoginData(self):
        user = str(input("User: "))
        passwd = getpass("Password: ")
        self.__loginData = {"user": user, "passwd": passwd}

    def getLoginData(self):
        return self.__loginData

    def set_meeting_code(self, **kwargs): raise NotImplementedError

    def set_login_url(self, **kwargs): self.__login_url = kwargs["url"]

    def get_login_url(self): return self.__login_url

    def set_driver(self, **kwargs):
        if kwargs["browser"] == "firefox": self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)
        else: self.__driver = None

    def get_driver(self): return self.__driver



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
        self.set_login_url(url="https://accounts.google.com/Login?hl=pt-BR")

    def execute(self, **kwargs):
        self.doLogin()

        try: self.get_driver.get(self.meet_url)
        except selenium.common.exceptions.InvalidArgumentException:
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            self.close_drive()
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        return

    def doLogin(self):
        start_time = self.get_time()
        self.get_driver.get(self.get_login_url())

        #USER
        try:
            self.get_driver.find_element_by_id("identifierId").send_keys(self.getLogiself.get_driver.find_element_by_name("password").send_keys(self.getLoginData()["user"]))
            self.get_driver.find_element_by_id("identifierNext").click()
            try:
                if self.get_driver.find_element_by_class_name("o6cuMc"):
                    print("ERROR ****** Login failed. Check user and try again! ******")
                    self.close_drive()
                    return
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("ERROR ****** Login failed. Check your connection and try again! ******")
            self.close_drive()
            return
            
        #PASSWORD
        for _ in range(15):
            try:
                self.get_driver.find_element_by_name("password").send_keys(self.getLoginData()["passwd"])
                break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException):
                sleep(1)
        try:
            self.get_driver.find_element_by_id("passwordNext").click()
            try:
                if self.get_driver.find_element_by_class_name("EjBTad"):
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
            self.meet_url =  ""
            return

        code_len = len(kwargs["meeting_code"])
        if code_len != 12 and code_len != 10:
            print("ERROR ****** Meeting code not accepted! Please check again ******")
            self.meet_url =  ""
        elif (code_len == 12 and kwargs["meeting_code"][3] == "-" and kwargs["meeting_code"][8] == "-") or code_len == 10:
            for crc in kwargs["meeting_code"]:
                try:
                    int(crc)
                    print("ERROR ****** Meeting code must not contain numbers! ******")
                    self.meet_url =  ""
                    return
                except ValueError: continue
            self.meet_url="https://meet.google.com/%s" % kwargs["meeting_code"]



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
        self.set_login_url(url="https://zoom.us/google_oauth_signin")

    def execute(self, **kwargs):
        self.doLogin()

        try:
            self.get_driver.get(self.meet_url)
            self.get_driver.find_elements_by_tag_name("a")[4].click()
        except (selenium.common.exceptions.InvalidArgumentException, selenium.common.exceptions.NoSuchElementException):
            print("ERROR ****** Meeting code was not properly set. Please, provide a valid one and try again! ******")
            self.close_drive()
            return
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        self.get_driver.find_element_by_id("joinBtn").click()
        return

    def set_meeting_code(self, **kwargs):
        if "https://zoom.us/j/" in kwargs["meeting_code"]:
            self.meet_url = kwargs["meeting_code"]
        else: self.meet_url="https://zoom.us/j/%s" % kwargs["meeting_code"]
