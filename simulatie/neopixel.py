from typing import Tuple


class _NeoPixelBase:
    """
    a class to add a few missing methods to the NeoPixel class
    """

    def __len__(self) -> int:
        """
        Returns the number of LEDs in the strip.
        """
        ...

    def __setitem__(self, index: int, val, /) -> None:
        """
        Set the pixel at *index* to the value, which is an RGB/RGBW tuple.
        """
        ...

    def __getitem__(self, index: int, /) -> Tuple:
        """
        Returns the pixel at *index* as an RGB/RGBW tuple.
        """
        ...


class NeoPixel(_NeoPixelBase):
    """
    This class stores pixel data for a WS2812 LED strip connected to a pin. The
    application should set pixel data and then call :meth:`NeoPixel.write`
    when it is ready to update the strip.

    For example::

        import neopixel

        # 32 LED strip connected to X8.
        p = machine.Pin.board.X8
        n = neopixel.NeoPixel(p, 32)

        # Draw a red gradient.
        for i in range(32):
            n[i] = (i * 8, 0, 0)

        # Update the strip.
        n.write()
    """

    ORDER: Incomplete
    pin: Incomplete
    n: Incomplete
    bpp: Incomplete
    buf: Incomplete
    timing: Incomplete

    def __init__(self, pin, n, bpp: int = 3, timing: int = 1) -> None:
        """
        Construct an NeoPixel object.  The parameters are:

            - *pin* is a machine.Pin instance.
            - *n* is the number of LEDs in the strip.
            - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
            - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
        """
        ...

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
        ...
