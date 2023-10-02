import jv_display.ledmatrix
from jv_display.display.display import Display, Pixel, Color
import time

matrix = jv_display.ledmatrix.led_matrix(
    # com_port="com3", 
    debug_connection=('localhost', 44444)
    )
display = Display()


while True:
    display << Color.Red
    matrix.show(display)
    time.sleep(2)

    # for i,r in enumerate(display.rows):
    #     r << Pixel( (0xFFFFFF // display.row_count) * i )
    rows = list(display.rows)[::2]
    for r in rows:
        r << 0x00FF00
    matrix.show(display)
    time.sleep(2)


    display[0,0] = Color.Red
    display[1,0] = Color.Blue
    display[0,1] = Color.Green

    matrix.show(display)
    time.sleep(3)