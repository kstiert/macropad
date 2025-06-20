from adafruit_hid.keyboard import Keyboard
from keypad import Keys
from neopixel import NeoPixels
from rotaryio import IncrementalEncoder


class Macropad:
    def __init__(self, keys: Keys, neopixels: NeoPixels, encoder: IncrementalEncoder, keyboard: Keyboard):
        self.keys = keys
        self.neopixels = neopixels
        self.encoder = encoder
        self.keyboard = keyboard
