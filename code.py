import board
import keypad
import neopixel
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_simple_text_display import SimpleTextDisplay

from csp.v1.clipstudiopaint import ClipStudioPaint
from macropad import Macropad

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

ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 20, 0)

encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.4)
kbd = Keyboard(usb_hid.devices)
macropad = Macropad(keys, neopixels, encoder, kbd)
handlers = [ClipStudioPaint(macropad)]
selected_handler = handlers[0]

last_position = encoder.position
text = SimpleTextDisplay("Macropad", title_scale=2)
text.show()
neopixels.fill(OFF_COLOR)

while True:
    position = encoder.position
    if position != last_position:
        if position > last_position:
            selected_handler.handle_rotary_increment()
        else:
            selected_handler.handle_rotary_decrement()
        last_position = position

    event = keys.events.get()
    if event:
        key_number = event.key_number
        # A key transition occurred.
        if event.pressed:
            selected_handler.handle_key_press(key_number)
            neopixels[key_number] = ON_COLOR

        if event.released:
            selected_handler.handle_key_release(key_number)
            neopixels[key_number] = OFF_COLOR
