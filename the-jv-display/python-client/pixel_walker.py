import jv_display.ledmatrix
from jv_display.display.display import Display, Pixel
import time

COM_PORT = 'com3'
DEBUG_HOST = 'localhost'
DEBUG_PORT = 44444

BLACK = [0x00, 0x00, 0x00]
RED = [0xFF, 0x00, 0x00]
GREEN = [0x00, 0xFF, 0x00]
BLEU = [0x00, 0x00, 0xFF]

YELLOW = [0xFF, 0xFF, 0x00]
PURPLE = [0x00, 0xFF, 0xFF]

matrix = jv_display.ledmatrix.led_matrix(
    com_port= COM_PORT, 
    debug_connection=(DEBUG_HOST, DEBUG_PORT)
    )
display = Display()

while True:
    display << PURPLE
    matrix.show(display)
    time.sleep(1)

    display[0,0] << RED
    display[1,1] << GREEN

    matrix.show(display)
    time.sleep(2)



    display << RED
    matrix.show(display)

    time.sleep(1)

    columns = display.columns
    c = next(columns)
    c << GREEN
    matrix.show(display)

    c = next(columns)
    c << GREEN
    matrix.show(display)

    c = next(columns)
    c << GREEN
    matrix.show(display)

    # time.sleep(1)

    rows = display.rows

    r = next(rows)
    r << YELLOW
    matrix.show(display)

    r = next(rows)
    r << YELLOW
    matrix.show(display)

    time.sleep(1)

    for r in list(display.rows)[::2]:
        r << PURPLE
    matrix.show(display)
    time.sleep(1)

    display[0,0] = (255,   0,   0)
    display[1,0] = (  0, 255,   0)
    display[0,1] = (  0,   0, 255)

    matrix.show(display)
    time.sleep(3)