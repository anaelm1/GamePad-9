import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner  # use kmk.scanners.matrix instead if your KMK version needs it
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from busio import I2C


# Initialize KMK keyboard instance
keyboard = KMKKeyboard()

# Add macro module
macros = Macros()
keyboard.modules.append(macros)

# Add encoder module
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Setup Rotary Encoder
# A = D8, B = D9, push button = D10
encoder_handler.pins = ((board.D8, board.D9, board.D10, False),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MNXT),)]  # Vol down, Vol up, click = Next track

# Define row and column pins
ROW_PINS = [board.D0, board.D1, board.D2]
COL_PINS = [board.D3, board.D6, board.D7]

keyboard.matrix = MatrixScanner(
    column_pins=COL_PINS,
    row_pins=ROW_PINS,
    columns_to_anodes=False,
)

# Define the keymap (3x3 matrix)
keyboard.keymap = [
    [
        KC.TAB,  KC.W,    KC.E,
        KC.A,    KC.S,    KC.D,
        KC.LSFT, KC.SPC,  KC.LCTL,
    ]
]

# OLED: SDA = D4, SCL = D5
i2c = I2C(scl=board.D5, sda=board.D4)
display = Display(
    display=SSD1306(i2c=i2c, device_addr=0x3C),
    entries=[
        TextEntry(text="GamePad 9", x=0, y=0, x_size=128, y_size=16),
        TextEntry(text="WASD Mode", x=0, y=24, x_size=128, y_size=16),
    ],
    width=128,
    height=64,
)
keyboard.extensions.append(display)

# Start KMK
if __name__ == '__main__':
    keyboard.go()