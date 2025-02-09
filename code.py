import board
import digitalio
import time
import usb_hid
from joystick_xl.hid import create_joystick
from joystick_xl.inputs import Button
from joystick_xl.joystick import Joystick

ledPorts = [board.GP16, board.GP17, board.GP18]
buttonPorts = [board.GP15, board.GP14, board.GP13]

# Create lists to store the LED and button objects
leds = []
buttons = []

# Setup LEDs
for ledPort in ledPorts:
    led = digitalio.DigitalInOut(ledPort)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

# Setup buttons
for buttonPort in buttonPorts:
    button = digitalio.DigitalInOut(buttonPort)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)

js = Joystick()
for button in buttons:
    js.add_input(Button(button))

while True:
    js.update()
    for i in range(len(leds)):
        leds[i].value = not buttons[i].value

