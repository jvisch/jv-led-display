from .pixel import Pixel
from .color import Color

class Display:

    def __init__(self, dimension, color) -> None:
        # dimension
        nr_of_rows, nr_of_cols = dimension
        if nr_of_rows < 1:
            raise ValueError('Row count must be greater or equal to 1')
        if nr_of_cols < 1:
            raise ValueError('Column count must be greater than 2')
        # Pixels
        columns = []
        for i in range(nr_of_cols):
            column = [Pixel(color) for _ in range(nr_of_rows)]
            columns.append(tuple(column))
        self._columns = tuple(columns)

    def __str__(self) -> str:
        rows_as_strings = ', '.join(map(str, self.rows))
        return f'[{rows_as_strings}]'

    @property
    def pixels(self):
        for i,column in enumerate(self._columns):
            if i % 2 == 1:
                column = reversed(column)
            for pixel in column:
                yield pixel

    @property
    def count(self):
        return self.row_count * self.column_count

    def __getitem__(self, index):
        x, y = index
        return self._columns[x][y]

    def __setitem__(self, index, pixel):
        x, y = index
        self._columns[x][y] << pixel

    def __len__(self):
        return self.count
    
    def __lshift__(self, value):
        for p in self.pixels:
            p << value

    def __bytes__(self):
        return bytes(self.raw_bytes)

    @property
    def raw_bytes(self):
        return [b for pixel in self.pixels for b in pixel]

    @property
    def row_count(self):
        return len(self._columns[0])

    @property
    def column_count(self):
        return len(self._columns)

    @property
    def rows(self):
        for r in range(self.row_count):
            row = tuple(column[r] for column in self._columns)
            yield DisplayPart(row)

    @property
    def columns(self):
        for column in self._columns:
            yield DisplayPart(column)

class DisplayPart:

    def __init__(self, pixels) -> None:
        self.__pixels = pixels

    def __str__(self) -> str:
        pixels_as_string = ', '.join(map(str, self.__pixels))
        return f'[{pixels_as_string}]'

    def __getitem__(self, index):
        return self.pixels[index]

    def __setitem__(self, index, pixel):
        self.__pixels[index] << pixel

    @property
    def pixels(self):
        return self.__pixels

    @property
    def count(self):
        return len(self.pixels)

    def __len__(self):
        return self.count

    def __lshift__(self, value):
        if isinstance(value, Pixel | int) or len(value) == 3:
            for p in self.pixels:
                p << value
        else:
            if not len(value) == len(self):
                raise ValueError('value length not equal to row length')
            for i in range(len(self)):
                self.pixels[i] << value[i]


# class Row(DisplayPart):

#     def __init__(self, row_index, display: Display):
#         start = display.index(0, row_index)
#         end = start + display.column_count
#         pixels = display.pixels[start: end]
#         super().__init__(pixels)


# class Column(DisplayPart):

#     def __init__(self, column_index, display: Display):
#         start = column_index
#         step = display.column_count
#         pixels = display.pixels[start:: step]
#         super().__init__(pixels)
