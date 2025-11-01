import machine
import neopixel

from .color import *


class Display:

    def __init__(self, row_count, column_count, pin: machine.Pin):
        """
        Initializes the matrix
        :param row_count: number of rows
        :param column_count: numer of columns
        :param pin: pin to communicate with
        :return: None
        """
        self.__columns = self.__create_indexes(row_count, column_count)
        n = row_count * column_count
        self._display = neopixel.NeoPixel(pin, n)

    @staticmethod
    def __create_indexes(row_count, column_count):
        columns = []
        for c in range(column_count):
            if c % 2 == 0:
                start = 0
                end = row_count
                step = 1
            else:
                start = row_count - 1
                end = -1
                step = -1
            elements = tuple(c * row_count + r for r in range(start, end, step))
            columns.append(elements)

        return tuple(columns)

    def row_count(self):
        return len(self.__columns[0])

    def column_count(self):
        return len(self.__columns)

    def show(self):
        """
        Shows the led pattern on the display
        :return: None
        """
        self._display.write()

    def pixel(self, column, row):
        from .pixel import Pixel
        pixel_index = self.__columns[column][row]
        return Pixel(self._display, pixel_index)

    def column(self, index):
        from .part import Part
        return Part(self._display, self.__columns[index])

    def row(self, index):
        row = (column[index] for column in self.__columns)
        from .part import Part
        return Part(self._display, row)

    def __getitem__(self, index):
        from .pixel import Pixel
        p = Pixel(self._display, index)
        return p

    def __lshift__(self, new_color):
        self.fill(new_color)

    def fill(self, value: Color):
        if not isinstance(value, RGB):
            value = value.to_rgb()
        self._display.fill(value.as_tuple())
        self.show()

    def reset(self):
        value = RGB(0, 0, 0)
        self.fill(value)
