
class Pixel:
    def __init__(self, red, green, blue) -> None:
        self << (red, green, blue)

    def __str__(self) -> str:
        return self.__rgb.hex()

    def __len__(self):
        return 3

    @property
    def red(self):
        return self.__rgb[0]

    @red.setter
    def red(self, value):
        self.__rgb[0] = value

    @property
    def green(self):
        return self.__rgb[1]

    @green.setter
    def green(self, value):
        self.__rgb[1] = value

    @property
    def blue(self):
        return self.__rgb[2]

    @blue.setter
    def blue(self, value):
        self.__rgb[2] = value

    def __lshift__(self, color):
        if isinstance(color, Pixel):
            rgb = color.__rgb.copy()
        elif isinstance(color, int):
            rgb = bytearray(color.to_bytes(3))
        else:
            rgb = bytearray(color)
        if len(rgb) != len(self):
            raise ValueError('Invalid argument')
        self.__rgb = rgb
