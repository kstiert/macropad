from macropad import Macropad

class HandlerBase():
    def __init__(self, name: str, macropad: Macropad):
        self._name = name
        self._macropad = macropad

    @property
    def name(self):
        return self._name
    
    @property
    def macropad(self):
        return self._macropad
    
    def handle_key_press(self, key_number: int):
        pass

    def handle_key_release(self, key_number: int):
        pass

    def handle_rotary_increment(self):
        pass

    def handle_rotary_decrement(self):
        pass