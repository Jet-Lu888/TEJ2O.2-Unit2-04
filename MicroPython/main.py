"""
Created by: Jet Lu
Created on: Feb 2026
This module is a Micro:bit MicroPython program that will tell you the temperature.
"""

from microbit import *

temperature = 0
import time

# reset
display.clear
display.show(Image.HAPPY)
time.sleep(1000)

# temperature will display when A is pressed
while True:
    if button_a.is_pressed():
        temperature = input.temperature()
        print("The temperature is")
        print(temperature)
        time.sleep(1000)
        display.clear  # reset
        display.show(Image.HAPPY)
