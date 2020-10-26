from delorean import Delorean
from time import sleep
import sys

from .browser_request import open_url

class clockwork():
    def __init__(self, URL = None, **kwargs):
        super().__init__()
        self.__time_now = Delorean().now()
        try:
            self.__target = self.__time_now.replace(hour = kwargs["hour"], minute = kwargs["minute"], second = kwargs["second"])
        except KeyError:
            print("Time not provided!")
            sys.exit(1)
        self.URL = URL

    def run(self):
        while True:
            self.get_time()
            print(self.__time_now.format_datetime(), "\n")
            if self.__time_now == self.__target or self.__time_now > self.__target:
                print("Time reached\nStarting service...")
                try:
                    open_url(self.URL)
                except:
                    print("ERROR TRYING TO GET URL")
                finally:
                    sys.exit(0)
            sleep(1)
    
    def get_time(self):
        self.__time_now = self.__time_now.now()
        self.__time_now.truncate("second")
    