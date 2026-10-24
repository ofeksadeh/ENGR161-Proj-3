# LightSensor.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
Light Sensor:
    Description:
        This sensor converts the light level at the bulb shaped detector into a voltage 
        which can then be read as an integer representing the total brightness.

    Hardware:
        Connect this sensor to any analog port on the Grove BaseHAT: A0, A2, A4, or A6.
        Initialize the sensor using only the number of the port, DO NOT include the A.
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Light_Sensor/
    
    Initialization:
        sensor_name = LightSensor(pin)

        If you plug your light sensor into A0 and want to name it 'light', your initialization 
        will look like this:

        light = LightSensor(0)

    LightSensor.light:
        Read the value from the light sensor, ranging from 0 to ~615. If your sensor name is 
        'light', accessing the light value will look like this:

        value_from_sensor = light.light
    
    LightSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
        
'''

### DO NOT MODIFY CODE BELOW THIS LINE ###
import time, sys, math
from grove.adc import ADC

class LightSensor(object):
    '''
    Grove Light Sensor class

    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC(address = 0x08)

    # Gets the current light strength percentage (0% or 100%)
    @property
    def light(self):
        '''
        Get the light strength value, maximum value is 100.0%

        Returns:
            (int): ratio, 0(0.0%) - 1000(100.0%)
        '''
        value = self.adc.read(self.channel)
        return value