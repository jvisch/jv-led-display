
class Pixel:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self << args[0]
        else:
            self << args

    def __str__(self) -> str:
        return self.__rgb.hex()

    def __len__(self):
        return 3

    def __iter__(self):
        return iter(self.__rgb)
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('rgb index out of range')
        return self.__rgb[index]

    @property
    def red(self):
        return self[0]

    @red.setter
    def red(self, value):
        self[0] = value

    @property
    def green(self):
        return self[1]

    @green.setter
    def green(self, value):
        self[1] = value

    @property
    def blue(self):
        return self[2]

    @blue.setter
    def blue(self, value):
        self[2] = value

    def __lshift__(self, color):
        # check input
        if isinstance(color, int):
            rgb = bytearray(color.to_bytes(3))
        else:
            rgb = bytearray(color)
        # check bytearray length
        if len(rgb) != len(self):
            raise ValueError('Invalid argument')
        self.__rgb = rgb
