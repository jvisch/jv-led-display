import jv_display.ledmatrix
from jv_display.display.color import rgb_to_hex
import colorsys

matrix = jv_display.ledmatrix.led_matrix(
    # com_port="com3",
    debug_connection=('localhost', 33333)
)

def blink(n=3):
    for _ in range(n):
        matrix << 0xffffff
        matrix.show()
        matrix << 0
        matrix.show()


def rows():
    def values(start, stop):
        while True:
            yield from range(start, stop)
            yield from range(stop, start, -1)
     
    for saturation in values(30, 100):
        for i, row in enumerate(matrix.rows):
            hsl = (i * 1/matrix.row_count, .5, saturation/100)
            rgb = colorsys.hls_to_rgb(*hsl)
            rgb = (int(255 * v) for v in rgb)
            color = rgb_to_hex(*rgb)

            row << color
        matrix.show()
        import time


blink(7)
rows()
