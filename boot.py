import usb_hid
from joystick_xl.hid import create_joystick

usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.MOUSE,
        usb_hid.Device.CONSUMER_CONTROL,
        create_joystick(axes=0, buttons=12, hats=0),
    )
)
