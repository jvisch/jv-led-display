from jv_led_display import *
from machine import Pin

def reset():
    p = Pin(0)
    d = Display(16, 16, p)
    d.reset()

reset()