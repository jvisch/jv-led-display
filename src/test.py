import time

from machine import Pin
from jv_led_display import display, color

d = display.Display(16, 16, Pin(0))

cnt = 0
for p in d:
    p.color = color.RGB(0, cnt, 0)
    cnt += 1
d.show()
