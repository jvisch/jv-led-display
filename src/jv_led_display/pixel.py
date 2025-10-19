import neopixel

from .color import Color, RGB, HSV


class Pixel:
    def __init__(self, display: neopixel.NeoPixel, index):
        self.__display = display
        self.__index = index

    @property
    def color(self) -> RGB:
        color = RGB(*self.__display[self.__index])
        return color

    @color.setter
    def color(self, value: Color):
        if not isinstance(value, RGB):
            value = value.to_rgb().as_tuple()
        self.__display[self.__index] = value.as_tuple()

    def __str__(self):
        return f'Pixel({self.__index}, {self.color}'
