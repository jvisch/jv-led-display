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
        self.__pixels = tuple(Pixel(*color) for _ in range(self.__real_size()))

    def __real_size(self):
        return self.row_count * self.column_count
    
    def __real_index(self, x, y):
        # just like a python list indexer
        if x < 0:
            x = self.column_count + x
        if x >= self.column_count:
            raise IndexError(f'x out of range)')
        if y < 0:
            y = self.row_count + y
        if y < 0 or y >= self.row_count:
            raise IndexError(f'y out of range)')
        # calculate index in the pixels array
        return (y * self.row_count) + x

    def __getitem__(self, index):
        array_index = self.__real_index(*index)
        return self.__pixels[array_index]
    
    def __setitem__(self, index, pixel):
        array_index = self.__real_index(*index)
        p = self.__pixels[array_index]
        # p.red = pixel.red
        # p.green = pixel.green
        # p.blue = pixel.blue
        p << pixel

    
    def __str__(self) -> str:
        pass
    
    @property
    def row_count(self):
        return self.__nr_of_rows

    @property
    def column_count(self):
        return self.__nr_of_cols

