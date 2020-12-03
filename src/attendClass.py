from sys import exit
from time import sleep
from clockwork import Clockwork
from selenium import webdriver
from datetime import timedelta

class AttendClass(Clockwork):
    def __init__(self, code, **kwargs):
        super().__init__(**kwargs)
        self.MEET_URL = self.assert_meeting_code(code, 10, 12)
        self.driver = webdriver.Chrome()

    def execute(self, **kwargs):
        self.driver.get(self.MEET_URL)
        self.shutdownConnection()
        return

    def shutdownConnection(self, **kwargs):
        self._Clockwork__target += timedelta(hours=1, minutes=30)
        while True:
            if self.get_time() == self._Clockwork__target:
                self.driver.close()
                return
            sleep(1)

    def assert_meeting_code(self, meeting_code, min_len, max_len):
        try: meeting_code + "STRING_TEST"
        except TypeError:
            print("Meeting code must be string!")
            exit(0)

        code_len = len(meeting_code)
        if code_len != max_len or code_len != min_len:
            print("Meeting code not accepted! Please check again")
            exit(0)
        elif (code_len == max_len and meeting_code[3] == "-" and meeting_code[8] == "-") or code_len == min_len:
            for crc in meeting_code:
                try:
                    int(crc)
                    print("Numbers are not accepted!")
                    exit(0)
                except ValueError: continue
            return "https://meet.google.com/%s" % meeting_code
