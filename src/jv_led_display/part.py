class Part:
    def __init__(self, matrix, indexes):
        self.__matrix = matrix
        self.__indexes = tuple(indexes)

    def __len__(self):
        return len(self.__indexes)

    def __getitem__(self, item):
        real_index = self.__indexes[item]
        pixel_color = self.__matrix[real_index]
        return pixel_color

    def __setitem__(self, key, value):
        real_index = self.__indexes[key]
        self.__matrix[real_index] = value

    def __str__(self):
        return str(self.__indexes)

    def __iter__(self):
        for i in self.__indexes:
            yield Pixel(self.__matrix, i)