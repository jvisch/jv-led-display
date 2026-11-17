import random
import time
import machine
import jv_led_display

MATRIX_W = 16
MATRIX_H = 16


def create_display():
    pin = machine.Pin(0)
    return jv_led_display.Display(MATRIX_W, MATRIX_H, pin)


def _heat_to_rgb(heat_value):
    # Zwart -> rood -> oranje -> geel/wit.
    if heat_value < 85:
        return heat_value * 3, 0, 0
    if heat_value < 170:
        return 255, (heat_value - 85) * 3, 0
    return 255, 255, (heat_value - 170) * 3


def fire(display, duration=15, frame_ms=30):
    heat = [0] * (MATRIX_W * MATRIX_H)
    end_time = time.time() + duration

    while time.time() < end_time:
        # Afkoelen
        for i in range(MATRIX_W * MATRIX_H):
            heat[i] = max(0, heat[i] - random.randint(0, 4))

        # Warmte stijgt omhoog (onderste rij in heat is y=0)
        for y in range(MATRIX_H - 1, 1, -1):
            for x in range(MATRIX_W):
                heat[y * MATRIX_W + x] = (
                    heat[(y - 1) * MATRIX_W + x]
                    + heat[(y - 2) * MATRIX_W + x]
                    + heat[(y - 2) * MATRIX_W + (x + 1) % MATRIX_W]
                ) // 3

        # Onderste rij aansteken
        for x in range(MATRIX_W):
            heat[x] = min(255, heat[x] + random.randint(160, 255))

        # Heatmap naar display schrijven
        for y in range(MATRIX_H):
            display_y = MATRIX_H - 1 - y
            for x in range(MATRIX_W):
                r, g, b = _heat_to_rgb(heat[y * MATRIX_W + x])
                display[x, display_y] << jv_led_display.RGB(r, g, b)

        display.show()
        time.sleep(frame_ms / 1000.0)

    display.reset()


def main(duration=15):
    print("Effect: vuur")
    display = create_display()
    fire(display, duration=duration)


# if __name__ == "__main__":
main()
