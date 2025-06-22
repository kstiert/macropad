import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keypad import Keys
from macropad.encoder import Encoder
from neopixel import NeoPixel

KEY_PINS = (
    board.KEY1,
    board.KEY2,
    board.KEY3,
    board.KEY4,
    board.KEY5,
    board.KEY6,
    board.KEY7,
    board.KEY8,
    board.KEY9,
    board.KEY10,
    board.KEY11,
    board.KEY12,
)

class MacropadHardware:
    def __init__(self):
        self._encoder = Encoder()
        self._keys = Keys(KEY_PINS, value_when_pressed=False, pull=True)
        self._neopixels = NeoPixel(board.NEOPIXEL, 12, brightness=0.4)
        self._hid = Keyboard(usb_hid.devices)

    @property
    def encoder(self) -> Encoder:
        return self._encoder
    
    @property
    def keys(self) -> Keys:
        return self._keys
    
    @property
    def neopixels(self) -> NeoPixel:
        return self._neopixels
    
    @property
    def keyboard(self) -> Keyboard:
        return self._hid
