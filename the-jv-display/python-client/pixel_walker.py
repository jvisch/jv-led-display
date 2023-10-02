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
display = Display()

while True:
    display << Color.Purple
    matrix.show(display)
    time.sleep(1)

    display[0,0] << Color.Red
    display[1,1] << Color.Green

    matrix.show(display)
    time.sleep(2)



    display << Color.Red
    matrix.show(display)

    time.sleep(1)

    columns = display.columns
    c = next(columns)
    c << Color.Green
    matrix.show(display)

    c = next(columns)
    c << Color.Green
    matrix.show(display)

    c = next(columns)
    c << Color.Green
    matrix.show(display)

    # time.sleep(1)

    rows = display.rows

    r = next(rows)
    r << Color.Yellow
    matrix.show(display)

    r = next(rows)
    r << Color.Yellow
    matrix.show(display)

    time.sleep(1)

    for r in list(display.rows)[::2]:
        r << Color.Purple
    matrix.show(display)
    time.sleep(1)

    display[0,0] = Color.Red
    display[1,0] = Color.Green
    display[0,1] = Color.Blue

    matrix.show(display)
    time.sleep(3)