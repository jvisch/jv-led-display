import jv_display.ledmatrix
from jv_display.display.display import Color
import time
import random

COM_PORT = 'com3'
DEBUG_HOST = 'localhost'
DEBUG_PORT = 44444

BLACK = Color.Black
RED = Color.Red
GREEN = Color.Green
BLUE = Color.Blue
YELLOW = Color.Yellow
PURPLE = Color.Purple
WHITE = Color.White

matrix = jv_display.ledmatrix.led_matrix(
    # com_port= COM_PORT, 
    debug_connection=(DEBUG_HOST, DEBUG_PORT)
    )

while True:
    x = random.randint(0, matrix.column_count - 1)
    y = random.randint(0, matrix.row_count - 1)
    matrix[x,y] << random.choice([RED, BLUE, GREEN, WHITE])
    matrix.show()