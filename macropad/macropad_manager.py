import macropad
from adafruit_simple_text_display import SimpleTextDisplay
from common.handler_base import HandlerBase
from macropad.macropad_hardware import MacropadHardware

class MacropadManager:
    def __init__(self):
        self._hardware = MacropadHardware()
        self._hardware.neopixels.fill(macropad.OFF_COLOR)

        self._handlers = []
        self._selected_handler = None

        self.text = SimpleTextDisplay()
        self.text[0].color = (255, 255, 255)
        self.text[1].color = (255, 255, 255)
        self.inMenu = False

    @property
    def hardware(self) -> MacropadHardware:
        return self._hardware
    
    def add_handler(self, handler: HandlerBase):
        handler.initialize(self._hardware)
        self._handlers.append(handler)
        if self._selected_handler is None:
            self._selected_handler = handler
    
    def update(self):
        self._handleEncoder()
        self._handleKeys()
        self._updateDisplay()
    
    def _handleEncoder(self):
        self.hardware.encoder.update()
        if self.hardware.encoder.button.pressed:
            self.inMenu = not self.inMenu

        if self.hardware.encoder.delta > 0:
            if self.inMenu:
                # Cycle through handlers in menu mode
                self._selected_handler = self._handlers[(self._handlers.index(self._selected_handler) + 1) % len(self._handlers)]
            else:
                # Handle rotary increment in normal mode
                self._selected_handler.handle_rotary_increment()
        elif self.hardware.encoder.delta < 0:
            if self.inMenu:
                # Cycle through handlers in menu mode
                self._selected_handler = self._handlers[(self._handlers.index(self._selected_handler) - 1) % len(self._handlers)]
            else:
                # Handle rotary decrement in normal mode
                self._selected_handler.handle_rotary_decrement()

    def _handleKeys(self):
        event = self.hardware.keys.events.get()
        if event:
            key_number = event.key_number

            if event.pressed:
                self._selected_handler.handle_key_press(key_number)
                self.hardware.neopixels[key_number] = macropad.ON_COLOR

            if event.released:
                self._selected_handler.handle_key_release(key_number)
                self.hardware.neopixels[key_number] = macropad.OFF_COLOR

    def _updateDisplay(self):
        self.text[0].text = self._selected_handler.name
        self.text[1].text = "Menu Mode" if self.inMenu else "Normal Mode"
        self.text.show()
