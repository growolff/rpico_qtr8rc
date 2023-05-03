from machine import Pin
from utime import sleep_us, ticks_us

class QTR8:
    def __init__(self, sensors, timeout=2500):
        print("Create qtr object")
        self.tOut = timeout
        self.pins = sensors
        self.s1 = Pin(self.pins[0],Pin.OUT)
        self.s2 = Pin(self.pins[1],Pin.OUT)
        self.s3 = Pin(self.pins[2],Pin.OUT)
        self.s4 = Pin(self.pins[3],Pin.OUT)
        self.s5 = Pin(self.pins[4],Pin.OUT)
        self.s6 = Pin(self.pins[5],Pin.OUT)
        self.sensor_array = [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6]
        self.sensor_values = [0,0,0,0,0,0]
    
    def readSensors(self):
        for idx, s in enumerate(self.sensor_array):
            self.sensor_values[idx] = self.read_sensor(idx)
        
        return self.sensor_values
    
    def read_sensor(self,n):
        self.sensor_array[n](1) # turn on the pin
        sleep_us(10) # charge condenser for 10 us
        self.sensor_array[n].init(self.sensor_array[n].IN) # make line an input
        t0 = ticks_us()
        time = 0
        while time < self.tOut:
            time = ticks_us() - t0
            if self.sensor_array[n].value() == 0:
                self.sensor_values[n] = time
                break
        self.sensor_array[n].init(self.sensor_array[n].OUT)
        return (self.sensor_values[n])
    
    def calibrate(self):
        pass