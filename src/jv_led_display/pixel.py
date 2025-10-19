import neopixel

from .color import Color, RGB, HSV


class Pixel:
    def __init__(self, display: neopixel.NeoPixel, index):
        self.__display = display
        self.__index = index

    @property
    def rgb(self) -> RGB:
        color = RGB(*self.__display[self.__index])
        return color

    @rgb.setter
    def rgb(self, value: Color):
        if not isinstance(value, RGB):
            value = value.to_rgb().as_tuple()
        self.__display[self.__index] = value.as_tuple()

    def __str__(self):
        return str(self.rgb)
