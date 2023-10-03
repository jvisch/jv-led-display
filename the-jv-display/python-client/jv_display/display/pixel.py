

class Pixel:

    def __init__(self, color) -> None:
        self << color

    def __str__(self) -> str:
        return f'0x{self.r:0{2}X}{self.g:0{2}X}{self.b:0{2}X}'

    def __len__(self):
        return 3

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

    # def __getitem__(self, index):
    #     if index < 0 or index >= len(self):
    #         raise IndexError('rgb index out of range')
    #     return self.__rgb[index]

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def __lshift__(self, color):
        self._b = (color & 0xFF)
        self._g = (color >> 8) & 0xFF
        self._r = (color >> 16) & 0xFF
