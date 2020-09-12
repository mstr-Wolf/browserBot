from delorean import Delorean
from time import sleep
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib import (read_file_content, open_url, last_date_recovery, DATETIME_NOW)

class clockwork():
    def __init__(self, timezone, givenURL, **kwargs):
        super().__init__()
        self.__time_now = Delorean(timezone=timezone)
        try:
            self.__target = Delorean(datetime = DATETIME_NOW,timezone=timezone).replace(hour = kwargs["hour"],
                                                                                    minute = kwargs["minute"],
                                                                                    second = kwargs["second"])
        except:
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
                    sys.exit(0)
                except:
                    print("ERROR TRYING TO OPEN URL")
                    sys.exit(1)
            sleep(1)
    
    def get_time(self):
        self.__time_now = self.__time_now.now()
        self.__time_now.truncate("second")
    
    def get_URL(self):
        return self.__URL
    URL = property(fget=get_URL)