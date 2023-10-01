import jv_display.ledmatrix
from jv_display.display.display import Display, Pixel
import time

matrix = jv_display.ledmatrix.led_matrix(
    com_port="com3", 
    # debug_connection=('localhost', 44444)
    )
display = Display()


while True:
    display << (255,0,0)
    matrix.show(display)
    time.sleep(2)

    # for i,r in enumerate(display.rows):
    #     r << Pixel( (0xFFFFFF // display.row_count) * i )
    rows = list(display.rows)[::2]
    for r in rows:
        r << 0x00FF00
    matrix.show(display)
    time.sleep(2)


    display[0,0] = (255,   0,   0)
    display[1,0] = (  0, 255,   0)
    display[0,1] = (  0,   0, 255)

    matrix.show(display)
    time.sleep(3)