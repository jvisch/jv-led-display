from jv_display.display.pixel import Pixel
from jv_display.display.display import Display

import serial
import time

COM = "com4"
BAUDRATE = 115200
SLEEPY = .015

with serial.Serial(COM, BAUDRATE) as s:
    time.sleep(2)
    d = Display()

    def show_display():
        s.write(d.raw_bytes)
        time.sleep(SLEEPY)

    prev = Pixel(0,0,0)
    for p in d.pixels:
        prev << 0
        p << 0xff0000
        show_display()
        prev = p
    
    for p in reversed(d.pixels):
        prev << 0
        p << 0xff0000
        show_display()
        prev = p
    