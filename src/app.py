import machine
import time

import jv_led_display

p = machine.Pin(0)
display = jv_led_display.Display(16, 16, p)
display.reset()

color = jv_led_display.RGB(0, 255, 0).to_hsv()

display << color

time.sleep(2)
display.reset()

column = display.column(2)
column << jv_led_display.RGB(0, 10, 0)
display.show()

time.sleep(2)

row = display.row(11)
row << jv_led_display.RGB(0, 0, 22)
display.show()

