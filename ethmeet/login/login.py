from getpass import getpass
from time import sleep
from abc import ABC, abstractmethod

import selenium.common.exceptions

from ..driver import Driver


class Login(ABC, Driver):
    def __init__(self, **kwargs):
        super(ABC).__init__()
        self.__login_data = {}
        self._login_url = None

        try:
            self._driver = kwargs["driver"]
        except (KeyError): pass

    @abstractmethod
    def doLogin(self): raise NotImplementedError

    @property
    def login_data(self): return self.__login_data

    @login_data.setter
    def login_data(self, data):
        try:
            self.__login_data = {"user": data["user"], "passwd": data["passwd"]} 
        except KeyError:
            user = str(input("User: "))
            passwd = getpass("Password: ")
            self.__login_data = {"user": user, "passwd": passwd}

    def _set_login_url(self, platform):
        plat_login = {
            "google": "https://accounts.google.com/Login?hl=pt-BR",
            "meet": "https://accounts.google.com/Login?hl=pt-BR",
            "zoom": "https://zoom.us/google_oauth_signin"
        }
        try: self._login_url = plat_login[platform]
        except KeyError:
            print("ERROR ****** ******** Platform not available! ******")


class LoginGoogle(Login):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._set_login_url("google")

    def doLogin(self):
        try: self._driver.get(self._login_url)
        except AttributeError:
            print("ERROR ****** WEB DIVER OR LOGIN URL UNSET! ******")
            return False

        #USER
        try:
            self._driver.find_element_by_id("identifierId").send_keys(self.login_data["user"])
            self._driver.find_element_by_id("identifierNext").click()
            try:
                if self._driver.find_element_by_class_name("o6cuMc"):
                    print("ERROR ****** Login failed. Check user and try again! ******")
                    return False
            except selenium.common.exceptions.NoSuchElementException: pass
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
            print("ERROR ****** Login failed. No element (o6cuMc) found! Couldn't stablish connection ******")
            return False

        #PASSWORD
        for _ in range(15):
            try:
                self._driver.find_element_by_name("password").send_keys(self.login_data["passwd"])
                break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException):
                sleep(1)
        for _ in range(15):
            try:
                self._driver.find_element_by_id("passwordNext").click()
                try:
                    if self._driver.find_element_by_class_name("EjBTad"):
                        print("ERROR ****** Login failed. Check your password and try again! ******")
                        return False
                except selenium.common.exceptions.NoSuchElementException: break
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):
                    print("ERROR ****** Login failed. No element (passwordNext) found! Trying again... ******")
                    sleep(1)
        return True
