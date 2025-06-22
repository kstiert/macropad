from csp.v1.clipstudiopaint import ClipStudioPaint
from noop_handler import NoopHandler
from macropad.macropad_manager import MacropadManager

macropad = MacropadManager()
macropad.add_handler(ClipStudioPaint())
macropad.add_handler(NoopHandler())

while True:
    macropad.update()
