import time
import socket

# import emulator.run
from .emulator import run as emulator_run
from .display import display
from .display.color import Color

SLEEPY = .030
BAUDRATE = 115200


class led_matrix():

    def __init__(self, com_port=None, debug_connection=None, dimension=(16, 16), color=Color.HotPink) -> None:
        if com_port is None and debug_connection is None:
            raise ValueError(
                "Either 'com_port' of 'debug_connecton' must be set.")
        # connection to Arduino matrix
        self.serial_port = None
        if com_port:
            import serial
            self.serial_port = serial.Serial(com_port, BAUDRATE)
        # connection to TKinter debug form
        self.socket = None
        if debug_connection:
            host, port = debug_connection
            emulator_run.run(host, port)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(debug_connection)
        # give ports time to initialize. Value experimental determined
        time.sleep(2.1)
        self._display = display.Display(dimension, color)

    def show(self):
        byte_data = bytes(self._display)
        # Arduino matrix
        if self.serial_port:
            self.serial_port.write(byte_data)
        # TKinter form
        if self.socket:
            self.socket.sendall(byte_data)
        # Let system process the data
        time.sleep(SLEEPY)

    def close(self):
        if self.serial_port:
            self.serial_port.close()
        if self.socket:
            self.socket.close()

    @property
    def display(self):
        return self._display

    # The display interface

    def __str__(self) -> str:
        return str(self.display)

    @property
    def pixels(self):
        return self.display.pixels

    @property
    def count(self):
        return self.display.count

    def __getitem__(self, index):
        return self.display[index]

    def __setitem__(self, index, pixel):
        self.display[index] = pixel

    def __len__(self):
        return self._display.count

    def __lshift__(self, value):
        self.display << value

    def __bytes__(self):
        return bytes(display)

    @property
    def raw_bytes(self):
        return self.display.raw_bytes

    @property
    def row_count(self):
        return self.display.row_count

    @property
    def column_count(self):
        return self._display.column_count

    @property
    def rows(self):
        return self.display.rows

    @property
    def columns(self):
        return self.display.columns
