from machine import Pin
from time import sleep

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    sleep(0.3)
    led.value(0)
    sleep(0.3)
