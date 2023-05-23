from .pixel import Pixel


class Display:

    def __init__(self, dimension=(16, 16), color=(0, 0, 0)) -> None:
        # dimension
        nr_of_rows, nr_of_cols = dimension
        if nr_of_rows < 1:
            raise ValueError('Row count must be greater or equal to 1')
        if nr_of_cols < 1:
            raise ValueError('Column count must be greater than 2')
        self.__nr_of_rows = nr_of_rows
        self.__nr_of_cols = nr_of_cols
        # Pixels
        if len(color) != 3:
            raise ValueError('Color must contain exactly 3 values (rgb)')
        self.__pixels = tuple(Pixel(*color) for _ in range(self.count))

    def __str__(self) -> str:
        rows_as_strings = ', '.join(map(str, self.rows))
        return f'[{rows_as_strings}]'

    @property
    def pixels(self):
        return self.__pixels

    @property
    def count(self):
        return self.row_count * self.column_count

    def index(self, x, y):
        # just like a python list indexer
        if x < 0:
            x = self.column_count + x
        if x >= self.column_count:
            raise IndexError(f'x out of range)')
        if y < 0:
            y = self.row_count + y
        if y >= self.row_count:
            raise IndexError(f'y out of range)')
        # calculate index in the pixels array
        return (y * self.row_count) + x

    def __getitem__(self, index):
        array_index = self.index(*index)
        return self.pixels[array_index]

    def __setitem__(self, index, pixel):
        array_index = self.index(*index)
        self.pixels[array_index] << pixel

    def __len__(self):
        return self.count

    @property
    def row_count(self):
        return self.__nr_of_rows

    @property
    def column_count(self):
        return self.__nr_of_cols

    @property
    def rows(self):
        for row_index in range(self.row_count):
            yield Row(row_index, self)

    @property
    def columns(self):
        for column_index in range(self.column_count):
            yield Column(column_index, self)


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
        if isinstance(value, Pixel):
            for p in self.pixels:
                p << value
        else:
            if not len(value) == len(self):
                raise ValueError('value length not equal to row length')
            for i in range(len(self)):
                self.pixels[i] << value[i]


class Row(DisplayPart):

    def __init__(self, row_index, display: Display):
        start = display.index(0, row_index)
        end = start + display.column_count
        pixels = display.pixels[start: end]
        super().__init__(pixels)


class Column(DisplayPart):

    def __init__(self, column_index, display: Display):
        start = column_index
        step = display.column_count
        pixels = display.pixels[start:: step]
        super().__init__(pixels)
