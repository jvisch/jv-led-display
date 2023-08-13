import socket
import time


from jv_display.display.display import Display
from jv_display.emulator.run import run

run()
time.sleep(2.1)

d = Display()
d << 0xff0000

HOST = 'localhost'    # The remote host
PORT = 65432            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    b = bytes(d)
    print(len(b))
    s.sendall(b)
    time.sleep(1)

    for i in range(1):
        # print(i)

        d << 0x000000
        d[0,i] << 0x00FF00
        s.sendall(bytes(d))

        d << 0x0000ff
        d[0,i] << 0x00FF00
        s.sendall(bytes(d))

        d << 0x00ff00
        d[0,i] << 0x00FF00
        s.sendall(bytes(d))

        d << 0xff0000
        d[0,i] << 0x00FF00
        s.sendall(bytes(d))

        d << 0xffff00
        d[0,i] << 0x00FF00
        s.sendall(bytes(d))

        d << 0xffffff
        d[0,i] << 0x00FF00
        s.sendall(bytes(d)[:-2])

        print(f'sleep {i}')
        time.sleep(10)
        # print(i)