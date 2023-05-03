from machine import Pin
from utime import sleep

from QTR import QTR8

sensor_pins = array('i',[2,3,4,5,6,7])
qtr8 = QTR8(sensor_pins,3000)

pin = Pin("LED", Pin.OUT)

while True:
    s1 = qtr8.readSensors()
    print(s1)
    
    sleep(0.001)