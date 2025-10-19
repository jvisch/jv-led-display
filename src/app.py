import machine
import time

import jv_led_display

p = machine.Pin(0)
m = jv_led_display.Display(16, 16, p)

r = m.row(2)
for p in r:
    p.color = jv_led_display.RGB(10, 0, 0)

m.show()
time.sleep(1)

c = m.column(4)
for p in c:
    p.color = jv_led_display.RGB(9, 0, 0)

m.show()

time.sleep(1)
m.reset()

m.fill(jv_led_display.RGB(4, 4, 9))
m.show()