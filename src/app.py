import machine
import jv_led_display

p = machine.Pin(0)
m = jv_led_display.Display(16, 16, p)
