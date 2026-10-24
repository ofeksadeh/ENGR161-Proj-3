# UltrasonicSensor.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###
'''
Ultrasonic Sensor:
    Description:
        This sensor can be used to determine the distance between the sensor and a surface in 
        front of it. This is done by emitting high frequecy sound and then detecting the reflected 
        sound, using the delay between transmission and reception to calculate the distance. This
        sensor outputs a distance in centimeters, with an accurate range between 3 cm and 350 cm.

    Hardware:
        Connect this sensor to any digital port on the Grove BaseHAT (any port starting with D)
        Initialize the sensor using only the number of the port, DO NOT include the D.
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.html
    
    Initialization:
        sensor_name = UltrasonicSensor(pin)

        If you plug your Ultrasonic Sensor into D5 and want to name it 'ultra', your initialization 
        will look like this:

        ultra = UltrasonicSensor(5)

    UltrasonicSensor.getDist:
        Read the value from the sensor, outputting the measured distance in cm. If your sensor's 
        name is 'ultra', accessing this value will look like this:

        dist = ultra.getDist

    UltrasonicSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
        
'''

import sys
import time
from grove.gpio import GPIO

# This usleep is to have used to have the sensor sleep for a certain amount of microseconds
usleep = lambda x: time.sleep(x / 1000000.0)

# These global variables are used as part of the distance calculations the sensor performs
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class UltrasonicSensor(object):
    def __init__(self, pin):
        self.dio = GPIO(pin)

    # This function calculates the distance that the nearest object it can detect is from the sensor in centimeters
    @property
    def getDist(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)

        self.dio.dir(GPIO.IN)

        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance