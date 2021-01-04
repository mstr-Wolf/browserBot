from delorean import Delorean
from time import sleep
import sys

class Clockwork():
    def __init__(self, **kwargs):
        self.__time_now = Delorean().now()
        try:
            self.__target = self.__time_now.replace(hour = kwargs["hour"], minute = kwargs["minute"], second = 0)
        except KeyError:
            print("Time not provided!")
            sys.exit()
        except (ValueError, TypeError):
            print("Invalid time values!")
            sys.exit()

    def run(self):
        print(__name__, "started!")
        print("Process scheduled to", self.__target.format_datetime(), "\n")
        while True:
            print(self.get_time().format_datetime(), end="\r")
            if self.__time_now >= self.__target:
                print("Time reached\nStarting process...")
                try:
                    self.execute()
                except:
                    print("ERROR TRYING TO GET URL")
                finally:
                    sys.exit(0)
            sleep(1)

    def execute(self, **kwargs):
        raise NotImplementedError

    def get_time(self):
        self.__time_now = self.__time_now.now()
        self.__time_now.truncate("second")
        return self.__time_now
