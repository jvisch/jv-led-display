import random
import sys
import time

try:
    import machine
except ImportError:
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]
    simulatie_path = project_root / "simulatie"
    if str(simulatie_path) not in sys.path:
        sys.path.insert(0, str(simulatie_path))
    import machine

import jv_led_display

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


def _new_drop(speed_min, speed_max):
    return {
        "head": random.uniform(-MATRIX_H, -1),
        "speed": random.uniform(speed_min, speed_max),
        "tail": random.randint(5, 10),
    }


def _fade_display(display, factor=0.6):
    for y in range(MATRIX_H):
        for x in range(MATRIX_W):
            current = display[x, y].color
            display[x, y] << jv_led_display.RGB(
                int(current.r * factor),
                int(current.g * factor),
                int(current.b * factor),
            )


def matrix_glitch_pulse(display, chance=0.03):
    if random.random() >= chance:
        return

    row = random.randint(0, MATRIX_H - 1)
    for x in range(MATRIX_W):
        display[x, row] << jv_led_display.RGB(80, 255, 80)

    for _ in range(random.randint(6, 14)):
        x = random.randint(0, MATRIX_W - 1)
        y = random.randint(0, MATRIX_H - 1)
        g = random.randint(40, 180)
        display[x, y] << jv_led_display.RGB(0, g, 0)


def matrix_intro(display, duration=2.0, frame_ms=60):
    end_time = time.time() + duration
    display.reset()

    while time.time() < end_time:
        _fade_display(display, factor=0.72)

        for x in range(MATRIX_W):
            if random.random() < 0.28:
                y = random.randint(0, MATRIX_H - 1)
                g = random.randint(80, 170)
                display[x, y] << jv_led_display.RGB(0, g, 0)

        if random.random() < 0.12:
            x = random.randint(0, MATRIX_W - 1)
            y = random.randint(0, MATRIX_H - 1)
            display[x, y] << jv_led_display.RGB(120, 255, 120)

        display.show()
        _sleep_ms(frame_ms)


def matrix_rain(display, duration=None, frame_ms=55, density=0.22, speed_min=0.35, speed_max=0.9):
    drops_active = [False] * MATRIX_W
    drops_head = [0.0] * MATRIX_W
    drops_speed = [0.0] * MATRIX_W
    drops_tail = [0] * MATRIX_W
    end_time = None if duration is None else time.time() + duration

    try:
        display.reset()
        while end_time is None or time.time() < end_time:
            _fade_display(display, factor=0.58)
            for x in range(MATRIX_W):
                if not drops_active[x] and random.random() < density:
                    drop = _new_drop(speed_min, speed_max)
                    drops_head[x] = drop["head"]
                    drops_speed[x] = drop["speed"]
                    drops_tail[x] = drop["tail"]
                    drops_active[x] = True

                if not drops_active[x]:
                    continue

                head = drops_head[x] + drops_speed[x]
                drops_head[x] = head
                head_y = int(head)
                tail = drops_tail[x]

                # Heldere kop met vervagende groene staart.
                for t in range(tail):
                    y = head_y - t
                    if y < 0 or y >= MATRIX_H:
                        continue

                    if t == 0:
                        color = jv_led_display.RGB(120, 255, 120)
                    else:
                        g = max(0, 210 - t * 28)
                        color = jv_led_display.RGB(0, g, 0)
                    display[x, y] << color

                if head_y - tail > MATRIX_H:
                    drops_active[x] = False

            # Zeldzame achtergrond-glyph voor extra Matrix-sfeer.
            if random.random() < 0.08:
                x = random.randint(0, MATRIX_W - 1)
                y = random.randint(0, MATRIX_H - 1)
                display[x, y] << jv_led_display.RGB(0, 20, 0)

            matrix_glitch_pulse(display, chance=0.03)

            display.show()
            _sleep_ms(frame_ms)
    finally:
        display.reset()


def main(duration=None):
    print("Effect: matrix rain")
    display = create_display()
    matrix_intro(display)
    matrix_rain(display, duration=duration)


# if __name__ == "__main__":
main(duration=None)

