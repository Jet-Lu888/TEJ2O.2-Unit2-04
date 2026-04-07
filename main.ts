/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Jet Lu
 * Created on: Feb 2026
 * This program will display the temperature.
*/

let temperature: number

// reset
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// temperature will display when button a is pressed
input.onButtonPressed(Button.A, function () {
  temperature = input.temperature()
  basic.clearScreen()
  basic.showString("The temperature is")
  basic.showNumber(temperature)
  pause(1000)
  basic.clearScreen()
  basic.showIcon(IconNames.Happy)
})
