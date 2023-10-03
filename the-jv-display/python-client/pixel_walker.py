import jv_display.ledmatrix
from jv_display.display.display import Display, Pixel, Color
import time

COM_PORT = 'com3'
DEBUG_HOST = 'localhost'
DEBUG_PORT = 44444

matrix = jv_display.ledmatrix.led_matrix(
    # com_port= COM_PORT, 
    debug_connection=(DEBUG_HOST, DEBUG_PORT)
    )

while True:
    matrix << Color.Purple
    matrix.show()
    time.sleep(1)

    matrix[0,0] << Color.Red
    matrix[1,1] << Color.Green

    matrix.show()
    time.sleep(2)



    matrix << Color.Red
    matrix.show()

    time.sleep(1)

    columns = matrix.columns
    c = next(columns)
    c << Color.Green
    matrix.show()

    c = next(columns)
    c << Color.Green
    matrix.show()

    c = next(columns)
    c << Color.Green
    matrix.show()

    # time.sleep(1)

    rows = matrix.rows

    r = next(rows)
    r << Color.Yellow
    matrix.show()

    r = next(rows)
    r << Color.Yellow
    matrix.show()

    time.sleep(1)

    for r in list(matrix.rows)[::2]:
        r << Color.Purple
    matrix.show()
    time.sleep(1)

    matrix[0,0] = Color.Red
    matrix[1,0] = Color.Green
    matrix[0,1] = Color.Blue

    matrix.show()
    time.sleep(3)