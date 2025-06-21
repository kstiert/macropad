from handler_base import HandlerBase
class NoopHandler(HandlerBase):
    def __init__(self, macropad):
        super().__init__("Noop", macropad)
    
    def handle_key_press(self, key_number: int):
        # No operation for key press
        pass

    def handle_key_release(self, key_number: int):
        # No operation for key release
        pass

    def handle_rotary_increment(self):
        # No operation for rotary increment
        pass

    def handle_rotary_decrement(self):
        # No operation for rotary decrement
        pass
