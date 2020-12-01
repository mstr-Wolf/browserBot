from delorean import Delorean
from time import sleep
import sys

class clockwork():
    def __init__(self, **kwargs):
        self.__time_now = Delorean().now()
        try:
            self.__target = self.__time_now.replace(hour = kwargs["hour"], minute = kwargs["minute"], second = 0)
        except KeyError:
            print("Time not provided!")
            sys.exit(1)

    def run(self):
        print(__name__, "process started on the background!")
        while True:
            self.get_time()

            if self.__time_now == self.__target or self.__time_now > self.__target:
                print("Time reached\nStarting service...")
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
    