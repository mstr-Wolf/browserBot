import sys
from time import sleep
from clockwork import Clockwork
from selenium import webdriver
from datetime import timedelta

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

class AttendClass(Clockwork):
    def __init__(self, code, class_length = 90, **kwargs):
        super().__init__(**kwargs)
        self.MEET_URL = assert_meeting_code(code, 10, 12)
        self.driver = None
        self.length = class_length

    def execute(self, **kwargs):
        self.driver = webdriver.Chrome()
        self.driver.get(self.MEET_URL)
        self.shutdownConnection(hours = self.get_class_duration()[0], minutes = self.get_class_duration()[1])
        return

    def shutdownConnection(self, **kwargs):
        self._Clockwork_target = self.get_time() + timedelta(hours=kwargs["hours"], minutes=kwargs["minutes"])
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
