from typing import Final, Callable, overload, TypeAlias, Any

Incomplete: TypeAlias = Any  # stable

class Pin:
    ALT_UART_AUX: Final[int] = 11
    ALT_USB: Final[int] = 10
    ALT_XIP_CS1: Final[int] = 9
    ALT_UART: Final[int] = 2
    ALT_SPI: Final[int] = 1
    PULL_DOWN: Final[int] = 2
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    OPEN_DRAIN: Final[int] = 2
    """Selects the pin mode."""
    OUT: Final[int] = 1
    """Selects the pin mode."""
    IN: Final[int] = 0
    """Selects the pin mode."""
    IRQ_RISING: Final[int] = 8
    """Selects the IRQ trigger type."""
    IRQ_FALLING: Final[int] = 4
    """Selects the IRQ trigger type."""
    ALT_CORESIGHT_TRACE: Final[int] = 9
    ALT_GPCK: Final[int] = 9
    ALT_HSTX: Final[int] = 0
    ALT: Final[int] = 3
    """Selects the pin mode."""
    PULL_UP: Final[int] = 1
    """\
    Selects whether there is a pull up/down resistor.  Use the value
    ``None`` for no pull.
    """
    ALT_SIO: Final[int] = 5
    ALT_PIO2: Final[int] = 8
    ALT_PWM: Final[int] = 4
    ALT_I2C: Final[int] = 3
    ALT_PIO1: Final[int] = 7
    ALT_PIO0: Final[int] = 6
    ALT_OPEN_DRAIN: Incomplete
    ANALOG: Incomplete
    PULL_HOLD: Incomplete
    DRIVE_0: int
    DRIVE_1: int
    DRIVE_2: int
    IRQ_LOW_LEVEL: Incomplete
    IRQ_HIGH_LEVEL: Incomplete
    def low(self) -> None:
        """
        Set pin to "0" output level.

        Availability: mimxrt, nrf, renesas-ra, rp2, samd, stm32 ports.
        """
        ...
    def irq(
        self,
        /,
        handler: Callable[[Pin], None] | None = None,
        trigger: int = (IRQ_FALLING | IRQ_RISING),
        *,
        priority: int = 1,
        wake: int | None = None,
        hard: bool = False,
    ) -> Callable[..., Incomplete]:
        """
           Configure an interrupt handler to be called when the trigger source of the
           pin is active.  If the pin mode is ``Pin.IN`` then the trigger source is
           the external value on the pin.  If the pin mode is ``Pin.OUT`` then the
           trigger source is the output buffer of the pin.  Otherwise, if the pin mode
           is ``Pin.OPEN_DRAIN`` then the trigger source is the output buffer for
           state '0' and the external pin value for state '1'.

           The arguments are:

             - ``handler`` is an optional function to be called when the interrupt
               triggers. The handler must take exactly one argument which is the
               ``Pin`` instance.

             - ``trigger`` configures the event which can generate an interrupt.
               Possible values are:

               - ``Pin.IRQ_FALLING`` interrupt on falling edge.
               - ``Pin.IRQ_RISING`` interrupt on rising edge.
               - ``Pin.IRQ_LOW_LEVEL`` interrupt on low level.
               - ``Pin.IRQ_HIGH_LEVEL`` interrupt on high level.

               These values can be OR'ed together to trigger on multiple events.

             - ``priority`` sets the priority level of the interrupt.  The values it
               can take are port-specific, but higher values always represent higher
               priorities.

             - ``wake`` selects the power mode in which this interrupt can wake up the
               system.  It can be ``machine.IDLE``, ``machine.SLEEP`` or ``machine.DEEPSLEEP``.
               These values can also be OR'ed together to make a pin generate interrupts in
               more than one power mode.

             - ``hard`` if true a hardware interrupt is used. This reduces the delay
               between the pin change and the handler being called. Hard interrupt
               handlers may not allocate memory; see :ref:`isr_rules`.
               Not all ports support this argument.

           This method returns a callback object.

        The following methods are not part of the core Pin API and only implemented on certain ports.
        """
        ...
    def toggle(self) -> Incomplete:
        """
        Toggle output pin from "0" to "1" or vice-versa.

        Availability: cc3200, esp32, esp8266, mimxrt, rp2, samd ports.
        """
        ...
    def off(self) -> None:
        """
        Set pin to "0" output level.
        """
        ...
    def on(self) -> None:
        """
        Set pin to "1" output level.
        """
        ...
    def init(
        self,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
    ) -> None:
        """
        Re-initialise the pin using the given parameters.  Only those arguments that
        are specified will be set.  The rest of the pin peripheral state will remain
        unchanged.  See the constructor documentation for details of the arguments.

        Returns ``None``.
        """
        ...

    @overload
    def value(self) -> int:
        """
        This method allows to set and get the value of the pin, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the digital logic level of
        the pin, returning 0 or 1 corresponding to low and high voltage signals
        respectively.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The method returns the actual input value currently present
            on the pin.
          - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
          - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
            return value of the method is undefined.  Otherwise, if the pin is in
            state '1', the method returns the actual input value currently present
            on the pin.

        If the argument is supplied then this method sets the digital logic level of
        the pin.  The argument ``x`` can be anything that converts to a boolean.
        If it converts to ``True``, the pin is set to state '1', otherwise it is set
        to state '0'.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
            pin state does not change, it remains in the high-impedance state.  The
            stored value will become active on the pin as soon as it is changed to
            ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
          - ``Pin.OUT`` - The output buffer is set to the given value immediately.
          - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
            state.  Otherwise the pin is set to high-impedance state.

        When setting the value this method returns ``None``.
        """

    @overload
    def value(self, x: Any, /) -> None:
        """
        This method allows to set and get the value of the pin, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the digital logic level of
        the pin, returning 0 or 1 corresponding to low and high voltage signals
        respectively.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The method returns the actual input value currently present
            on the pin.
          - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
          - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
            return value of the method is undefined.  Otherwise, if the pin is in
            state '1', the method returns the actual input value currently present
            on the pin.

        If the argument is supplied then this method sets the digital logic level of
        the pin.  The argument ``x`` can be anything that converts to a boolean.
        If it converts to ``True``, the pin is set to state '1', otherwise it is set
        to state '0'.  The behaviour of this method depends on the mode of the pin:

          - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
            pin state does not change, it remains in the high-impedance state.  The
            stored value will become active on the pin as soon as it is changed to
            ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
          - ``Pin.OUT`` - The output buffer is set to the given value immediately.
          - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
            state.  Otherwise the pin is set to high-impedance state.

        When setting the value this method returns ``None``.
        """
    def high(self) -> None:
        """
        Set pin to "1" output level.

        Availability: mimxrt, nrf, renesas-ra, rp2, samd, stm32 ports.
        """
        ...

    class cpu:
        GPIO20: Pin  ## = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO25: Pin  ## = Pin(GPIO25, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO26: Pin  ## = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO27: Pin  ## = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO24: Pin  ## = Pin(GPIO24, mode=ALT, alt=31)
        GPIO21: Pin  ## = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO22: Pin  ## = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO23: Pin  ## = Pin(GPIO23, mode=ALT, alt=31)
        GPIO28: Pin  ## = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO6: Pin  ## = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO7: Pin  ## = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO8: Pin  ## = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO5: Pin  ## = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO29: Pin  ## = Pin(GPIO29, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO3: Pin  ## = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO4: Pin  ## = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO9: Pin  ## = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO2: Pin  ## = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO1: Pin  ## = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO10: Pin  ## = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO11: Pin  ## = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO0: Pin  ## = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        EXT_GPIO0: Pin  ## = Pin(EXT_GPIO0, mode=IN)
        EXT_GPIO1: Pin  ## = Pin(EXT_GPIO1, mode=IN)
        EXT_GPIO2: Pin  ## = Pin(EXT_GPIO2, mode=IN)
        GPIO12: Pin  ## = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO17: Pin  ## = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO18: Pin  ## = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO19: Pin  ## = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO16: Pin  ## = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO13: Pin  ## = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO14: Pin  ## = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GPIO15: Pin  ## = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        def __init__(self, *argv, **kwargs) -> None: ...

    class board:
        GP3: Pin  ## = Pin(GPIO3, mode=ALT, pull=PULL_DOWN, alt=31)
        GP28: Pin  ## = Pin(GPIO28, mode=ALT, pull=PULL_DOWN, alt=31)
        GP4: Pin  ## = Pin(GPIO4, mode=ALT, pull=PULL_DOWN, alt=31)
        GP5: Pin  ## = Pin(GPIO5, mode=ALT, pull=PULL_DOWN, alt=31)
        GP22: Pin  ## = Pin(GPIO22, mode=ALT, pull=PULL_DOWN, alt=31)
        GP27: Pin  ## = Pin(GPIO27, mode=ALT, pull=PULL_DOWN, alt=31)
        GP26: Pin  ## = Pin(GPIO26, mode=ALT, pull=PULL_DOWN, alt=31)
        WL_GPIO2: Pin  ## = Pin(EXT_GPIO2, mode=IN)
        WL_GPIO0: Pin  ## = Pin(EXT_GPIO0, mode=IN)
        LED: Pin  ## = Pin(EXT_GPIO0, mode=IN)
        WL_GPIO1: Pin  ## = Pin(EXT_GPIO1, mode=IN)
        GP6: Pin  ## = Pin(GPIO6, mode=ALT, pull=PULL_DOWN, alt=31)
        GP7: Pin  ## = Pin(GPIO7, mode=ALT, pull=PULL_DOWN, alt=31)
        GP9: Pin  ## = Pin(GPIO9, mode=ALT, pull=PULL_DOWN, alt=31)
        GP8: Pin  ## = Pin(GPIO8, mode=ALT, pull=PULL_DOWN, alt=31)
        GP12: Pin  ## = Pin(GPIO12, mode=ALT, pull=PULL_DOWN, alt=31)
        GP11: Pin  ## = Pin(GPIO11, mode=ALT, pull=PULL_DOWN, alt=31)
        GP13: Pin  ## = Pin(GPIO13, mode=ALT, pull=PULL_DOWN, alt=31)
        GP14: Pin  ## = Pin(GPIO14, mode=ALT, pull=PULL_DOWN, alt=31)
        GP0: Pin  ## = Pin(GPIO0, mode=ALT, pull=PULL_DOWN, alt=31)
        GP10: Pin  ## = Pin(GPIO10, mode=ALT, pull=PULL_DOWN, alt=31)
        GP1: Pin  ## = Pin(GPIO1, mode=ALT, pull=PULL_DOWN, alt=31)
        GP21: Pin  ## = Pin(GPIO21, mode=ALT, pull=PULL_DOWN, alt=31)
        GP2: Pin  ## = Pin(GPIO2, mode=ALT, pull=PULL_DOWN, alt=31)
        GP19: Pin  ## = Pin(GPIO19, mode=ALT, pull=PULL_DOWN, alt=31)
        GP20: Pin  ## = Pin(GPIO20, mode=ALT, pull=PULL_DOWN, alt=31)
        GP15: Pin  ## = Pin(GPIO15, mode=ALT, pull=PULL_DOWN, alt=31)
        GP16: Pin  ## = Pin(GPIO16, mode=ALT, pull=PULL_DOWN, alt=31)
        GP18: Pin  ## = Pin(GPIO18, mode=ALT, pull=PULL_DOWN, alt=31)
        GP17: Pin  ## = Pin(GPIO17, mode=ALT, pull=PULL_DOWN, alt=31)
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(
        self,
        id: Any,
        /,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int | None = None,
        alt: int | None = None,
    ) -> None:
        """
        Access the pin peripheral (GPIO pin) associated with the given ``id``.  If
        additional arguments are given in the constructor then they are used to initialise
        the pin.  Any settings that are not specified will remain in their previous state.

        The arguments are:

          - ``id`` is mandatory and can be an arbitrary object.  Among possible value
            types are: int (an internal Pin identifier), str (a Pin name), and tuple
            (pair of [port, pin]).

          - ``mode`` specifies the pin mode, which can be one of:

            - ``Pin.IN`` - Pin is configured for input.  If viewed as an output the pin
              is in high-impedance state.

            - ``Pin.OUT`` - Pin is configured for (normal) output.

            - ``Pin.OPEN_DRAIN`` - Pin is configured for open-drain output. Open-drain
              output works in the following way: if the output value is set to 0 the pin
              is active at a low level; if the output value is 1 the pin is in a high-impedance
              state.  Not all ports implement this mode, or some might only on certain pins.

            - ``Pin.ALT`` - Pin is configured to perform an alternative function, which is
              port specific.  For a pin configured in such a way any other Pin methods
              (except :meth:`Pin.init`) are not applicable (calling them will lead to undefined,
              or a hardware-specific, result).  Not all ports implement this mode.

            - ``Pin.ALT_OPEN_DRAIN`` - The Same as ``Pin.ALT``, but the pin is configured as
              open-drain.  Not all ports implement this mode.

            - ``Pin.ANALOG`` - Pin is configured for analog input, see the :class:`ADC` class.

          - ``pull`` specifies if the pin has a (weak) pull resistor attached, and can be
            one of:

            - ``None`` - No pull up or down resistor.
            - ``Pin.PULL_UP`` - Pull up resistor enabled.
            - ``Pin.PULL_DOWN`` - Pull down resistor enabled.

          - ``value`` is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial
            output pin value if given, otherwise the state of the pin peripheral remains
            unchanged.

          - ``drive`` specifies the output power of the pin and can be one of: ``Pin.LOW_POWER``,
            ``Pin.MED_POWER`` or ``Pin.HIGH_POWER``.  The actual current driving capabilities
            are port dependent.  Not all ports implement this argument.

          - ``alt`` specifies an alternate function for the pin and the values it can take are
            port dependent.  This argument is valid only for ``Pin.ALT`` and ``Pin.ALT_OPEN_DRAIN``
            modes.  It may be used when a pin supports more than one alternate function.  If only
            one pin alternate function is supported the this argument is not required.  Not all
            ports implement this argument.

        As specified above, the Pin class allows to set an alternate function for a particular
        pin, but it does not specify any further operations on such a pin.  Pins configured in
        alternate-function mode are usually not used as GPIO but are instead driven by other
        hardware peripherals.  The only operation supported on such a pin is re-initialising,
        by calling the constructor or :meth:`Pin.init` method.  If a pin that is configured in
        alternate-function mode is re-initialised with ``Pin.IN``, ``Pin.OUT``, or
        ``Pin.OPEN_DRAIN``, the alternate function will be removed from the pin.
        """

    @overload
    def __call__(self) -> int:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """

    @overload
    def __call__(self, x: Any, /) -> None:
        """
        Pin objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Pin.value([x]).
        See :meth:`Pin.value` for more details.
        """

    @overload
    def mode(self) -> int:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def mode(self, mode: int, /) -> None:
        """
        Get or set the pin mode.
        See the constructor documentation for details of the ``mode`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def pull(self) -> int:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def pull(self, pull: int, /) -> None:
        """
        Get or set the pin pull state.
        See the constructor documentation for details of the ``pull`` argument.

        Availability: cc3200, stm32 ports.
        """

    @overload
    def drive(self, drive: int, /) -> None:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """
        ...

    @overload
    def drive(self, /) -> int:
        """
        Get or set the pin drive strength.
        See the constructor documentation for details of the ``drive`` argument.

        Availability: cc3200 port.
        """
