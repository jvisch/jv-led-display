from typing import Tuple, TypeAlias, Any
import threading
import tkinter
import os
import signal

import PixelDisplayFrame
import jv_led_display.pixel

Incomplete: TypeAlias = Any  # stable


class NeoPixel():

    def __init__(self, pin, n, bpp: int = 3, timing: int = 1) -> None:
        _, _, _ = pin, n, timing

        if bpp != 3:
            raise ValueError(
                "Unsupported bpp value: only RGB strips with bpp == 3 are supported"
            )
        assert n == (16*16), "Alleen displays van 16x16 worden ondersteund"
        self.led_strip = [(0, 0, 0)] * n

        # The form will be started on a separate thread
        self.form = None
        ready = threading.Event()

        def __start_form(np: NeoPixel):
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

        self.display_thread = threading.Thread(
            target=__start_form, args=(self,))
        self.display_thread.start()

        # wait for form thread to finish initialization
        ready.wait()

    def __len__(self) -> int:
        return len(self.led_strip)

    def __setitem__(self, i, v) -> None:
        """
        Set the pixel at *index* to the value, which is an RGB/RGBW tuple.
        """
        self.led_strip[i] = v

    def __getitem__(self, i) -> Tuple:
        """
        Returns the pixel at *index* as an RGB/RGBW tuple.
        """
        return self.led_strip[i]

    def fill(self, v) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        self.led_strip = [v] * len(self.led_strip)

    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        # For the simulation there is no gamma and lineair
        # correction neccesary, invert it back.
        cf = jv_led_display.pixel._inv_css_rgb
        colors = [cf(r, g, b) for r, g, b in self.led_strip]
        self.form.write_threadsafe(colors)
