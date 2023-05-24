# circuitpython demo
import time
import digitalio
import board

relay1 = digitalio.DigitalInOut(board.GP6)
relay1.direction = digitalio.Direction.OUTPUT
relay2 = digitalio.DigitalInOut(board.GP7)
relay2.direction = digitalio.Direction.OUTPUT
while True:
    relay1.value = True
    relay2.value = True
    time.sleep(0.5)
    relay1.value = False
    relay2.value = False
    time.sleep(0.5)
