from abc import ABC, abstractmethod

class AttendMeet(ABC):
    def __init__(self, **kwargs):
        self.meet_url = None
        try:
            self.driver = kwargs["driver"].driver
        except (AttributeError, KeyError): pass

        try: self.set_meeting_url(kwargs["code"])
        except KeyError: pass


    @abstractmethod
    def goto_meet(self): raise NotImplementedError

    @abstractmethod
    def set_meeting_url(self, code): raise NotImplementedError
