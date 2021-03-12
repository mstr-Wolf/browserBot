class Graver():
    def __init__(self):
        self.__drivers = {}

    @property
    def drivers(self):
        return self.__drivers