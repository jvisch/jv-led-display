import machine
import time

import jv_led_display

p = machine.Pin(0)
m = jv_led_display.Display(16, 16, p)

p = m.pixel(3, 3)

p << jv_led_display.RGB(10, 0, 3)

m.show()

time.sleep(1)

c = m.column(2)
c << jv_led_display.RGB(0, 10, 0)

r = m.row(11)
r << jv_led_display.RGB(0, 0, 22)
