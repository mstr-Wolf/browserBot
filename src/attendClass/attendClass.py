import sys
from datetime import timedelta
from time import sleep

import selenium.common.exceptions
from clockwork import Clockwork
from selenium import webdriver


class AttendClass(Clockwork):
    def __init__(self, code = "aaabbbbccc", class_length = 90, **kwargs):
        """
        Parameters:\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'kwargs["hour"]' (int): Class' start hour\n
            'kwargs["minute"]' (int): Class' start minute\n
        """
        super().__init__(**kwargs)
        self.MEET_URL = assert_meeting_code(code, 10, 12)
        self.driver = None
        self.length = class_length

    def execute(self, **kwargs):
        self.driver = webdriver.Chrome()
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

def assert_meeting_code(meeting_code, min_len, max_len):
    try: meeting_code + "STRING_TEST"
    except TypeError:
        print("Meeting code must be string!")
        sys.exit(0)

    code_len = len(meeting_code)
    if code_len != max_len and code_len != min_len:
        print("Meeting code not accepted! Please check again")
        sys.exit(0)
    elif (code_len == max_len and meeting_code[3] == "-" and meeting_code[8] == "-") or code_len == min_len:
        for crc in meeting_code:
            try:
                int(crc)
                print("Numbers are not accepted!")
                sys.exit(0)
            except ValueError: continue
        return "https://meet.google.com/%s" % meeting_code

class AutomaticLogin(AttendClass):
    def __init__(self, user_login, user_passwd, automatic_wait_time = 3, code = "aaabbbbccc", class_length = 90, **kwargs):
        """
        Parameters:\n
            'user_login' (string): User's e-mail or phone number\n
            'user_passwd' (string): User's password\n
            'automatic_wait_time' (int): wait time between 'doLogin()' method steps\n
            'code' (string): Meeting code\n
            'class_length' (float): Class lenght (in minutes)\n
            'kwargs["hour"]' (int): Class' start hour\n
            'kwargs["minute"]' (int): Class' start minute\n
        """
        super().__init__(code, class_length, **kwargs)

        self.passwd = user_passwd
        self.login = user_login
        self.wait_time = automatic_wait_time
        self.login_url = "https://accounts.google.com/Login?hl=pt-BR"

    def execute(self, **kwargs):
        start_time = self._Clockwork__time_now
        self.driver = webdriver.Chrome()
        self.doLogin()

        self.driver.get(self.MEET_URL)
        #enter class

        print("Login time: ", self.get_time() - start_time)
        shutTime = self.get_class_duration()
        self.shutdownConnection(hours = shutTime[0], minutes = shutTime[1])
        return

    def doLogin(self):
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("identifierId").send_keys(self.login)
        self.driver.find_element_by_id("identifierNext").click()

        try:
            self.driver.find_element_by_name("password").send_keys(self.passwd)
        except selenium.common.exceptions.NoSuchElementException:
            sleep(self.wait_time)
            self.driver.find_element_by_name("password").send_keys(self.passwd)
        self.driver.find_element_by_id("passwordNext").click()

        sleep(self.wait_time)
        self.driver.get("https://meet.google.com")
