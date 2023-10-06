import jv_display.ledmatrix
import jv_display.display.color
import colorsys

matrix = jv_display.ledmatrix.led_matrix(
    com_port="com3",
    debug_connection=('localhost', 33333)
)
count = matrix.row_count

step = 1 / count
hsl = [0, .5, 1]
for row in matrix.rows:
    rgb = colorsys.hls_to_rgb(*hsl)
    # print(f'{hsl} -> {rgb}')
    rgb = (round(255 * v) for v in rgb)
    row << jv_display.display.color.rgb_to_hex(*rgb)
    hsl[0] += step

matrix.show()

while True: None