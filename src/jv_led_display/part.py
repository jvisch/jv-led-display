import neopixel


class Part:
    def __init__(self, display: neopixel.NeoPixel, indexes):
        self.__display = display
        self.__indexes = tuple(indexes)

    def __len__(self):
        return len(self.__indexes)

    def __getitem__(self, index):
        from .pixel import Pixel
        real_index = self.__indexes[index]
        p = Pixel(self.__display, real_index)
        return p

    def __str__(self):
        return str(self.__indexes)

    def __iter__(self):
        from .pixel import Pixel
        for i in self.__indexes:
            yield Pixel(self.__display, i)
