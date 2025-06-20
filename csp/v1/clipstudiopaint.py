from adafruit_hid.keycode import Keycode

from macropad import MacroPad

KEYCODES = (
    (Keycode.P,),
    (Keycode.S,),
    (Keycode.E,),
    (Keycode.M,),
    (Keycode.U,),
    (Keycode.CONTROL, Keycode.Y),
    (Keycode.MINUS,),
    (Keycode.QUOTE,),
    (Keycode.CONTROL, Keycode.Z),
    (Keycode.CONTROL, Keycode.MINUS),
    (Keycode.CONTROL, Keycode.EQUALS),
    (Keycode.SPACE,),
)

ROT_UP_KEY = (Keycode.ALT, Keycode.CONTROL, Keycode.MINUS)
ROT_DOWN_KEY = (Keycode.ALT, Keycode.CONTROL, Keycode.EQUALS)


class ClipStudioPaint:
    def __init__(self, macropad: MacroPad):
        self.macropad = macropad

    def handle_key_press(self, key_number: int):
        self.macropad.keyboard.press(*KEYCODES[key_number])

    def handle_key_release(self, key_number: int):
        self.macropad.keyboard.release(*KEYCODES[key_number])

    def handle_rotary_increment(self):
        self.macropad.keyboard.press(*ROT_UP_KEY)
        self.macropad.keyboard.release(*ROT_UP_KEY)

    def handle_rotary_decrement(self):
        self.macropad.keyboard.press(*ROT_DOWN_KEY)
        self.macropad.keyboard.release(*ROT_DOWN_KEY)
