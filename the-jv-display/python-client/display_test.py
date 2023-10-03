import jv_display.ledmatrix
from jv_display.display.display import Color
import time

matrix = jv_display.ledmatrix.led_matrix(
    # com_port="com3", 
    debug_connection=('localhost', 44444)
    )

while True:
    matrix << Color.Red
    matrix.show()
    time.sleep(2)

    # for i,r in enumerate(display.rows):
    #     r << Pixel( (0xFFFFFF // display.row_count) * i )
    rows = list(matrix.rows)[::2]
    for r in rows:
        r << 0x00FF00
    matrix.show()
    time.sleep(2)


    matrix[0,0] = Color.Red
    matrix[1,0] = Color.Blue
    matrix[0,1] = Color.Green

    matrix.show()
    time.sleep(3)