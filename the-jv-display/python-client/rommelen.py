import jv_display.ledmatrix
from jv_display.display.display import Display, Pixel
import time
import random

COM_PORT = 'com3'
DEBUG_HOST = 'localhost'
DEBUG_PORT = 44444

BLACK = [0x00, 0x00, 0x00]
RED = [0xFF, 0x00, 0x00]
GREEN = [0x00, 0xFF, 0x00]
BLEU = [0x00, 0x00, 0xFF]

YELLOW = [0xFF, 0xFF, 0x00]
PURPLE = [0x00, 0xFF, 0xFF]
WHITE = 0xFFFFFF

matrix = jv_display.ledmatrix.led_matrix(
    # com_port= COM_PORT, 
    debug_connection=(DEBUG_HOST, DEBUG_PORT)
    )
display = Display()

while True:
    x = random.randint(0, display.column_count - 1)
    y = random.randint(0, display.row_count - 1)
    display[x,y] << random.choice([RED, BLEU, GREEN, WHITE])
    matrix.show(display)