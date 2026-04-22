import machine
import time

import jv_led_display

MATRIX_W = 16
MATRIX_H = 16

p = machine.Pin(0)
display = jv_led_display.Display(MATRIX_W, MATRIX_H, p)

def rainbow_diagonal():
    max_dist = (MATRIX_W - 1) + (MATRIX_H - 1)   # = 30
    for y in range(MATRIX_H):
        for x in range(MATRIX_W):
            t = (x + y) / max_dist          # 0.0 (rood) .. 1.0 (violet)
            hue = t * 270 / 360             # HSV verwacht 0.0..1.0, niet graden
            c = jv_led_display.HSV(hue, 1.0, 255)
            print(c)
            display[x,y] << c
    display.show()


print("Effect: regenboog diagonaal")
rainbow_diagonal()