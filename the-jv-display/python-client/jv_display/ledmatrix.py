import time
import socket

# import emulator.run
from .emulator import run as emulator_run
from .display import display

class led_matrix():

    def __init__(self, com_port=None, debug_connection=None) -> None:
        if com_port is None and debug_connection is None:
            raise ValueError(
                "Either 'com_port' of 'debug_connecton' must be set.")
        # connection to Arduino matrix
        if com_port:
            self.serial_port = None
            raise NotImplementedError("todo")
        # connection to TKinter debug form
        if debug_connection:
            host, port = debug_connection
            emulator_run.run(host, port)
            time.sleep(2.1)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(debug_connection)

    def show(self, display: display.Display):
        byte_data = bytes(display)
        # Arduino matrix
        if self.serial_port:
            raise NotImplementedError("todo")
        # TKinter form
        if self.socket:
            self.socket.sendall(byte_data)


    def close(self):
        if self.serial_port:
            raise NotImplementedError("todo")
        if self.socket:
            self.socket.close()
