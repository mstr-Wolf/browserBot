from delorean import Delorean
from time import sleep
import sys

from .file_actions import DATETIME_NOW
from .browser_request import open_url

class clockwork():
    def __init__(self, timezone, givenURL, **kwargs):
        super().__init__()
        self.__time_now = Delorean(timezone=timezone)
        try:
            self.__target = Delorean(datetime = DATETIME_NOW,timezone=timezone).replace(hour = kwargs["hour"],
                                                                                    minute = kwargs["minute"],
                                                                                    second = kwargs["second"])
        except KeyError:
            print("Time not provided!")
            sys.exit(1)
        self.__URL = givenURL
    
    def run(self):
        while True:
            self.get_time()
            print(self.__time_now.format_datetime(), "\n")
            if self.__time_now == self.__target or self.__time_now > self.__target:
                print("Time reached\nStarting service...")
                try:
                    open_url(self.URL)
                except:
                    print("ERROR TRYING TO OPEN URL")
                    raise
                finally:
                    sys.exit(0)
            sleep(1)
    
    def get_time(self):
        self.__time_now = self.__time_now.now()
        self.__time_now.truncate("second")
    
    def get_URL(self):
        return self.__URL
    URL = property(fget=get_URL)