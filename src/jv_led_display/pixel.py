import neopixel


class Pixel:
    def __init__(self, display: neopixel.NeoPixel, index):
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
