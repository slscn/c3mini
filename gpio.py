import time
from machine import Pin 

led=Pin(2,Pin.OUT)
print("hello myLED")

while True:
 
 led.value(1)
 time.sleep(1)
 led.value(0)
 time.sleep(1)

 