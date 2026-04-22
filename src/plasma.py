import time
import machine
import math

import jv_led_display

jv_led_display.pixel.BRIGHTNESS = .1

MATRIX_W = 16
MATRIX_H = 16


def _sleep_ms(milliseconds):
    if hasattr(time, "sleep_ms"):
        time.sleep_ms(milliseconds)
    else:
        time.sleep(milliseconds / 1000.0)


def create_display():
    pin = machine.Pin(0)
    return jv_led_display.Display(MATRIX_W, MATRIX_H, pin)


# --- Plasma-effect (golvende sinuspatronen) ---

def plasma(display):
    t = 0.0
    while True:
        for y in range(MATRIX_H):
            for x in range(MATRIX_W):
                v  = math.sin(x * 0.5 + t)
                v += math.sin(y * 0.5 + t * 0.7)
                v += math.sin((x + y) * 0.3 + t * 1.3)
                v += math.sin(math.sqrt(x * x + y * y) * 0.4 + t)
                hue = (v + 4) / 8  # HSV hue verwacht 0.0..1.0
                c = jv_led_display.HSV(hue, 1.0, 255)
                display[x, y] << c
        display.show()

        t += 0.15
        _sleep_ms(30)

    display.reset()
    display.show()

def main(duration=15):
    print("Effect: plasma")
    display = create_display()
    plasma(display)


# if __name__ == "__main__":
main()
