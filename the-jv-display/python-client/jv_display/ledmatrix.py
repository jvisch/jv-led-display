import time
import socket

# import emulator.run
from .emulator import run as emulator_run
from .display import display

SLEEPY = .030
BAUDRATE = 115200

class led_matrix():

    def __init__(self, com_port=None, debug_connection=None) -> None:
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
        

    def show(self, display: display.Display):
        byte_data = bytes(display)
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
