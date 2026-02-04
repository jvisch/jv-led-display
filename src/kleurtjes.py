import machine
import time

from jv_led_display import *

p = machine.Pin(0)
m = Display(16, 16, p)

kleurtjes = {
    'Black': (0, 0, 0),
    'White': (255, 255, 255),
    'Red': (255, 0, 0),
    'Lime': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Yellow': (255, 255, 0),
    'Cyan': (0, 255, 255),
    'Magenta': (255, 0, 255),
    'Silver': (192, 192, 192),
    'Gray': (128, 128, 128),
    'Maroon': (128, 0, 0),
    'Olive': (128, 128, 0),
    'Green': (0, 128, 0),
    'Purple': (128, 0, 128),
    'Teal': (0, 128, 128),
    'Navy': (0, 0, 128),
}


def run():
    print('start')
    for naam, rgb in kleurtjes.items():
        rgb = RGB(*rgb)
        print(f'{naam} : {rgb}')
        m << rgb
        time.sleep(5)
        print('done')

run()
