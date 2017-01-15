import time
import CHIP_IO.GPIO as GPIO
button_chan = "XIO-P0"
pull_chan = "XIO-P6"
GPIO.setup(button_chan , GPIO.IN)
GPIO.setup(pull_chan , GPIO.IN)

button_pressed = False
while True:
    button_pin = GPIO.input(button_chan)
    if (button_pin == 0):
        print("BUTTON IS PRESSED")
    pull_pin = GPIO.input(pull_chan)
    if (pull_pin == 1):
        print("PULL IS PULLED")
    #GPIO.wait_for_edge(button_chan, GPIO.RISING if button_pressed else GPIO.FALLING)
    #button_pressed = not button_pressed
    #print("button pressed is: ")
    #print(button_pressed)
    #if button_pressed:
    #    print("hooray it's time for beer")


