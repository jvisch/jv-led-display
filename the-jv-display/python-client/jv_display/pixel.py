class Pixel:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f'{self.red:02X}{self.green:02X}{self.blue:02X}'

    def __check_value_and_raise_exception(value):
        if value < 0 or value > 255:
            raise ValueError('Value must be between 0 and 255')

    @property
    def red(self):
        return self._r

    @red.setter
    def red(self, value):
        Pixel.__check_value_and_raise_exception(value)
        self._r = value

    @property
    def green(self):
        return self._g

    @green.setter
    def green(self, value):
        Pixel.__check_value_and_raise_exception(value)
        self._g = value

    @property
    def blue(self):
        return self._b

    @blue.setter
    def blue(self, value):
        Pixel.__check_value_and_raise_exception(value)
        self._b = value

    def __lshift__(self, pixel):
        self.red = pixel.red
        self.green = pixel.green
        self.blue = pixel.blue