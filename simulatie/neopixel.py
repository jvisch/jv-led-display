from typing import Tuple, TypeAlias, Any
import threading
import tkinter
import os
import signal 

import PixelDisplayFrame

Incomplete: TypeAlias = Any  # stable

class NeoPixel():
    ORDER: Incomplete
    pin: Incomplete
    n: Incomplete
    bpp: Incomplete
    buf: Incomplete
    timing: Incomplete

    def __init__(self, pin, n, bpp: int = 3, timing: int = 1) -> None:
        _, _, _,_ = pin, n, bpp, timing

        # The form will be started on a seperate thread
        self.form = None
        ready = threading.Event()
        def __start_form(np:NeoPixel):
            # create and initialize form
            root = tkinter.Tk()
            np.form = PixelDisplayFrame.PixelDisplayFrame(root)
            np.form.pack(side="top", fill="both", expand=True)

            # kill the whole process if the form is closed
            def on_close():
                os.kill(os.getpid(), signal.SIGTERM)
            root.protocol("WM_DELETE_WINDOW", on_close)
            
            # signal form initialized
            ready.set()
            # run user interface
            root.mainloop()

        self.display_thread = threading.Thread(target=__start_form, args=(self,))
        self.display_thread.start()
        
        # wait for form thread to finish initialization
        ready.wait()

    def __len__(self) -> int:
        """
        Returns the number of LEDs in the strip.
        """
        ...

    def __setitem__(self, i, v) -> None:
        """
        Set the pixel at *index* to the value, which is an RGB/RGBW tuple.
        """
        ...

    def __getitem__(self, i) -> Tuple:
        """
        Returns the pixel at *index* as an RGB/RGBW tuple.
        """
        ...

    def fill(self, v) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...

    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        self.form.write(list(range(10)))
