from keypad import Keys
from neopixel import NeoPixels
from rotaryio import IncrementalEncoder
from adafruit_hid.keyboard import Keyboard

class Macropad:
    def __init__(self,  keys: Keys, neopixels: NeoPixels, encoder: IncrementalEncoder, keyboard: Keyboard):
        self.keys = keys
        self.neopixels = neopixels
        self.encoder = encoder
        self.keyboard = keyboard
