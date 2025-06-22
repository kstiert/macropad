import board
import digitalio
from adafruit_debouncer import Button
from rotaryio import IncrementalEncoder

class Encoder:
    def __init__(self):
        self._encoder = IncrementalEncoder(board.ROTA, board.ROTB)
        self._position = self._encoder.position
        self._previousPosition = self._position
        encoderPin = digitalio.DigitalInOut(board.BUTTON)
        encoderPin.switch_to_input(pull=digitalio.Pull.UP)
        self._encoderButton = Button(encoderPin)

    @property
    def encoder(self) -> int:
        return self._position
    
    @property
    def delta(self) -> int:
        return self._encoder.position - self._previousPosition
    
    @property
    def delta_abs(self) -> int:
        return abs(self.delta)
    
    @property
    def button(self) -> Button:
        return self._encoderButton
    
    def update(self):
        self._encoderButton.update()
        self._previousPosition = self._position
        self._position = self._encoder.position

