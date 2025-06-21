import board
import digitalio
import keypad
import neopixel
import rotaryio
import usb_hid
from adafruit_debouncer import Button
from adafruit_hid.keyboard import Keyboard
from adafruit_simple_text_display import SimpleTextDisplay

from csp.v1.clipstudiopaint import ClipStudioPaint
from noop_handler import NoopHandler
from handler_base import HandlerBase
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
encoderPin = digitalio.DigitalInOut(board.BUTTON)
encoderPin.switch_to_input(pull=digitalio.Pull.UP)
encoderButton = Button(encoderPin)

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.4)
kbd = Keyboard(usb_hid.devices)
macropad = Macropad(keys, neopixels, encoder, kbd)
handlers: list[HandlerBase] = [ClipStudioPaint(macropad), NoopHandler(macropad)]
selected_handler = handlers[0]

menu = False
last_position = encoder.position
text = SimpleTextDisplay()
text[0].color = (255, 255, 255)
text[1].color = (255, 255, 255)
text.show()
neopixels.fill(OFF_COLOR)

while True:
    encoderButton.update()
    if encoderButton.pressed:
        menu = not menu
  
    position = encoder.position
    if position != last_position:
        if position > last_position:
            if menu:
                # Cycle through handlers in menu mode
                selected_handler = handlers[(handlers.index(selected_handler) + 1) % len(handlers)]
            else:
                # Handle rotary increment in normal mode
                selected_handler.handle_rotary_increment()
        else:
            if menu:
                # Cycle through handlers in menu mode
                selected_handler = handlers[(handlers.index(selected_handler) - 1) % len(handlers)]
            else:
                # Handle rotary decrement in normal mode
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

    text[0].text = selected_handler.name
    text[1].text = "Menu Mode" if menu else "Normal Mode"
    text.show()
