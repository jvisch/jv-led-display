import tkinter
from jv_display_emulator.pixel_display_frame import PixelDisplayFrame

if __name__ == "__main__":
    root = tkinter.Tk()
    d = PixelDisplayFrame(root)
    d.pack(side="top", fill="both", expand=True)
    d.write( [33,33,33,0xff, 0xff, 0xff] )
    root.mainloop()
    