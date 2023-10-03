import tkinter
import threading

from . import pixel_display_frame


def run(host, port):

    def show():
        root = tkinter.Tk()
        d = pixel_display_frame.PixelDisplayFrame(root, host=host, port=port)
        d.pack(side="top", fill="both", expand=True)
        # root.after(2000, d.handle_socket)
        root.mainloop()

    t = threading.Thread(target=show, daemon=True)
    t.start()
