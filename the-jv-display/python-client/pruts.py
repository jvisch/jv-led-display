from jv_display.emulator import run
from jv_display.display.display import Display
import socket

run.run()


import time
time.sleep(10)
print('done')

d = Display()
d << 0xff0000

HOST = 'localhost'    # The remote host
PORT = 65432            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    b = bytes(d)
    print(len(b))
    s.sendall(b)
    import time
    time.sleep(5)

    while True:
        d << 0x000000
        s.sendall(bytes(d))
        d << 0x0000ff
        s.sendall(bytes(d))
        d << 0x00ff00
        s.sendall(bytes(d))
        d << 0xff0000
        s.sendall(bytes(d))
        d << 0xffff00
        s.sendall(bytes(d))
        d << 0xffffff
        s.sendall(bytes(d))
