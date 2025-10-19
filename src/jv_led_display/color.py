class Color:

    def to_rgb(self):
        raise NotImplemented()

    def to_hsv(self):
        raise NotImplemented()


class RGB(Color):
    def __init__(self, r: int, g: int, b: int):
        self.r, self.g, self.b = r, g, b

    def __str__(self):
        return f'RGB({self.r}, {self.g}, {self.b})'

    def to_rgb(self):
        return self

    def as_tuple(self):
        return self.r, self.g, self.b

    def to_hsv(self):
        def rgb_to_hsv(r, g, b):
            maxc = max(r, g, b)
            minc = min(r, g, b)
            rangec = (maxc - minc)
            v = maxc
            if minc == maxc:
                return 0.0, 0.0, v
            s = rangec / maxc
            rc = (maxc - r) / rangec
            gc = (maxc - g) / rangec
            bc = (maxc - b) / rangec
            if r == maxc:
                h = bc - gc
            elif g == maxc:
                h = 2.0 + rc - bc
            else:
                h = 4.0 + gc - rc
            h = (h / 6.0) % 1.0
            return h, s, v

        hsv = rgb_to_hsv(self.r, self.g, self.b)
        return HSV(*hsv)


class HSV(Color):
    def __init__(self, h: float, s: float, v: float):
        self.h, self.s, self.v = h, s, v

    def __str__(self):
        return f'HSV({self.h}, {self.s}, {self.v})'

    def to_rgb(self):
        # copied from default library colorsys.py
        # https://github.com/python/cpython/blob/69d263cfe1ecbbf957a1f05a23cbea70a3bf6582/Lib/colorsys.py
        def hsv_to_rgb(h, s, v):
            if s == 0.0:
                return v, v, v
            i = int(h * 6.0)  # XXX assume int() truncates!
            f = (h * 6.0) - i
            p = v * (1.0 - s)
            q = v * (1.0 - s * f)
            t = v * (1.0 - s * (1.0 - f))
            i = i % 6
            if i == 0:
                return v, t, p
            if i == 1:
                return q, v, p
            if i == 2:
                return p, v, t
            if i == 3:
                return p, q, v
            if i == 4:
                return t, p, v
            if i == 5:
                return v, p, q
            # Cannot get here

        r, g, b = hsv_to_rgb(self.h, self.s, self.v)
        r = round(r)
        g = round(g)
        b = round(b)
        return RGB(r, g, b)

    def to_hsv(self):
        return self
