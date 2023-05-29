import tkinter
from . import pixel_display_frame

def show():
    root = tkinter.Tk()
    d = pixel_display_frame.PixelDisplayFrame(root)
    d.pack(side="top", fill="both", expand=True)
    root.mainloop()

def run():
    import threading
    t = threading.Thread(target=show)
    t.start()
    
if __name__ == "__main__":
    show()