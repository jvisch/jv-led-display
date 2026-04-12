import neopixel

from .color import Color, RGB, HSV

BRIGHTNESS = 0.25  # 0.0 .. 1.0
GAMMA = 2.2


class Pixel:
    def __init__(self, display: neopixel.NeoPixel, index):
        self.__display = display
        self.__index = index

    def __lshift__(self, new_color):
        self.color = new_color

    @property
    def color(self) -> RGB:
        r, g, b = _inv_css_rgb(*self.__display[self.__index])
        color = RGB(r, g, b)
        return color

    @color.setter
    def color(self, value: Color):
        # if HSV, convert to RGB first
        if not isinstance(value, RGB):
            value = value.to_rgb()
        r, g, b = value.as_tuple()
        css_value = _css_rgb(r, g, b)
        print(value)
        print(value.to_rgb())
        print(r, b, g)
        print(css_value)
        self.__display[self.__index] = css_value

    def __str__(self):
        return f'Pixel({self.__index}, {self.color}'


def _clamp8(value):
    if value < 0:
        return 0
    if value > 255:
        return 255
    return int(value)


def _gamma8(value):
    linear = _clamp8(value) / 255
    corrected = linear ** GAMMA
    return int(corrected * 255 + 0.5)


def _inv_gamma8(value):
    # Rekent de gamma-correctie terug naar de originele lineaire waarde.
    corrected = _clamp8(value) / 255
    linear = corrected ** (1.0 / GAMMA)
    return int(linear * 255 + 0.5)


def _css_rgb(r, g, b):
    # Convert CSS RGB to corrected NeoPixel tuple.
    r = _gamma8(_clamp8(r) * BRIGHTNESS)
    g = _gamma8(_clamp8(g) * BRIGHTNESS)
    b = _gamma8(_clamp8(b) * BRIGHTNESS)
    return r, g, b


def _inv_css_rgb(r, g, b):
    # Rekent een NeoPixel-tuple terug naar de originele CSS RGB-waarden (0-255).
    r = _clamp8(round(_inv_gamma8(r) / BRIGHTNESS))
    g = _clamp8(round(_inv_gamma8(g) / BRIGHTNESS))
    b = _clamp8(round(_inv_gamma8(b) / BRIGHTNESS))
    return r, g, b
