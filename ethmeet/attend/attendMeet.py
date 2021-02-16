from abc import ABC, abstractmethod

from ..driver import Driver

class AttendMeet(ABC, Driver):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.meet_url = None

        try:
            self.driver = kwargs["driver"]
        except (KeyError): pass

        try: self.set_meeting_url(kwargs["code"])
        except KeyError: pass


    @abstractmethod
    def goto_meet(self): raise NotImplementedError

    @abstractmethod
    def set_meeting_url(self, code): raise NotImplementedError
