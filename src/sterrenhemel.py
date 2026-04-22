import machine
import random
import time

import jv_led_display

MATRIX_W = 16
MATRIX_H = 16

p = machine.Pin(0)
display = jv_led_display.Display(MATRIX_W, MATRIX_H, p)

# Overwegend wit, zeldzame subtiele tint
# Gewichten: 70% puur wit, 15% blauwwit, 10% warmwit, 5% gelig
_STAR_COLORS = (
    [jv_led_display.RGB(255, 255, 255)] * 14 +
    [jv_led_display.RGB(210, 225, 255)] * 3 +
    [jv_led_display.RGB(255, 240, 220)] * 2 +
    [jv_led_display.RGB(255, 255, 210)] * 1
)

# Sterrenstadia: verschijnen, even branden, dan doven
_FADE_IN  = 0
_HOLD     = 1
_FADE_OUT = 2


def _new_star(used):
    """Maak een nieuwe ster op een vrije positie."""
    for _ in range(200):
        x = random.randint(0, MATRIX_W - 1)
        y = random.randint(0, MATRIX_H - 1)
        if (x, y) not in used:
            used.add((x, y))
            color = random.choice(_STAR_COLORS)
            peak = random.uniform(0.4, 1.0)
            fade_speed = random.uniform(0.02, 0.08)
            hold_frames = random.randint(10, 60)
            # [x, y, color, bright, phase, peak, fade_speed, hold_frames]
            return [x, y, color, 0.0, _FADE_IN, peak, fade_speed, hold_frames]
    return None


def starfield(num_stars=70, duration=20):
    used = set()
    stars = []
    while len(stars) < num_stars:
        s = _new_star(used)
        if s:
            # Begin op willekeurig punt in levenscyclus zodat beeld direct gevuld is
            s[3] = random.uniform(0.0, s[5])
            s[4] = random.choice([_HOLD, _FADE_OUT])
            stars.append(s)

    end_time = time.time() + duration
    while time.time() < end_time:
        display.reset()

        dead = []
        for star in stars:
            x, y, color, bright, phase, peak, fade_speed, hold_frames = star

            if phase == _FADE_IN:
                bright = min(bright + fade_speed, peak)
                if bright >= peak:
                    phase = _HOLD
            elif phase == _HOLD:
                hold_frames -= 1
                if hold_frames <= 0:
                    phase = _FADE_OUT
            else:  # FADE_OUT
                bright = max(bright - fade_speed, 0.0)
                if bright <= 0.0:
                    dead.append(star)

            star[3] = bright
            star[4] = phase
            star[7] = hold_frames

            dimmed = jv_led_display.RGB(
                int(color.r * bright),
                int(color.g * bright),
                int(color.b * bright),
            )
            display[x, y] << dimmed

        # Vervang gedoofde sterren direct door nieuwe
        for star in dead:
            stars.remove(star)
            used.discard((star[0], star[1]))
            s = _new_star(used)
            if s:
                stars.append(s)

        display.show()
        time.sleep(0.05)

    display.reset()


print("Effect: sterrenhemel")
starfield(num_stars=70, duration=20)