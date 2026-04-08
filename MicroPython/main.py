"""
Created by: Jet Lu
Created on: Feb 2026
This module is a Micro:bit MicroPython program that will tell you the temperature.
"""

from microbit import *

currentTemperature = 0

# reset
display.clear
display.show(Image.HAPPY)
sleep(1000)

# temperature will display when A is pressed
while True:
    if button_a.was_pressed():
        currentTemperature = temperature()
        display.scroll("The temperature is")
        display.scroll(currentTemperature)
        sleep(1000)
        display.clear  # reset
        display.show(Image.HAPPY)
