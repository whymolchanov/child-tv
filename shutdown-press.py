# FILEOVERVIEW
# Must be executed in background. Wait until button on 21 pin
# will be pressed and shut down system after that.
from gpiozero import Button
import os

Button(21).wait_for_press()
os.system("sudo shutdown -h now")
