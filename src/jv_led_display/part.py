class Part:
    def __init__(self, matrix, indexes):
        self.__matrix = matrix
        self.__indexes = tuple(indexes)

    def __len__(self):
        return len(self.__indexes)

    def __getitem__(self, item):
        from .pixel import Pixel
        real_index = self.__indexes[item]
        p = Pixel(self.__matrix, real_index)
        return p

    def __str__(self):
        return str(self.__indexes)

    def __iter__(self):
        from .pixel import Pixel
        for i in self.__indexes:
            yield Pixel(self.__matrix, i)