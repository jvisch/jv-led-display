from .display import Display


class Pixel:
    def __init__(self, display: Display, index: int) -> None:
        self.__display = display
        self.__index = index

    @property
    def rgb(self):
        return self.__display[self.__index]

    @rgb.setter
    def rgb(self, value):
        self.__display[self.__index] = value

    def __str__(self):
        return str(self.rgb)
