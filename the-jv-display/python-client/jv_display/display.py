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

    def __str__(self) -> str:
        pass

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


class Row:
    def __init__(self, row_index, display: Display):
        start = display.index(0, row_index)
        end = start + display.column_count
        self.__pixels = display.pixels[start : end]

    def __str__(self) -> str:
        return ' '.join(map(str, self.__pixels))
    
    def __getitem__(self, index):
        return self.pixels[index]

    def __setitem__(self, index, pixel):
        self.__pixels[index] << pixel

    @property
    def pixels(self):
        return self.__pixels