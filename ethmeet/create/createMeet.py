from abc import ABC, abstractmethod

class CreateMeet(ABC):
    def __init__(self, **kwargs):
        self.__code = None

    @abstractmethod
    def new_class(self):
        return

    def set_new_class(self, code):
        self.__code = code

    @property
    def code(self):
        try:
            return self.__code
        except AttributeError:
            print("Code unset!")
            return None
