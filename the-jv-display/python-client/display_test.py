import socket
import jv_display.display
import jv_display.emulator.run

jv_display.emulator.run.run()

d = jv_display.display.Display()
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

    d << 0x00ff00
    s.sendall(bytes(d))