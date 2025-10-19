import machine
import neopixel

from .part import Part


class Display:

    def __init__(self, row_count: int, column_count: int, pin: machine.Pin) -> None:
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
    def __create_indexes(row_count: int, column_count: int) -> tuple[tuple[int, ...], ...]:
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

    def column(self, index):
        return Part(self, self.__columns[index])

    def row(self, index):
        row = (column[index] for column in self.__columns)
        return Part(self, row)

    def __setitem__(self, key, value):
        self._display[key] = value

    def __getitem__(self, item):
        return self._display[item]
