# IRSensor.py

# Created by Seth McConkey on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
IR Sensor:
    Description:
        This sensor has two values that can be accessed: a value from 0 to 255 that is 
        proportional to the intensity of infrared light the left sensor is reading, and a value 
        from 0 to 255 that is proportional to the intensity of infrared light the right sensor is 
        reading. It is used to determine presence/distance of a strong infrared source, such as an 
        LED light or Infrared Beacon. In typical indoor conditions, it is not surprising to get a 
        zero from both sides of the sensor, but some value should be read in the sun or in the 
        presence of a powerful source.

    Hardware:
        Connect this sensor to any analog port on the Grove BaseHAT: A0, A2, A4, or A6.
        Initialize the sensor using only the number of the port, DO NOT include the A.
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/


    Initialization:

        sensor_name = IRSensor(pin, pin + 1)

        If you plug your IR Sensor into A0 and want to name it 'IR', your initialization will
        look like this:

        IR = IRSensor(0, 1)
    
    IRSensor.value1:
        Read the value from the sensor labeled sensor1. If your sensor's name is 'IR', accessing the left
        value will look like this:

        value_from_sensor1 = IR.value1

    IRSensor.value2:
        Read the value from the sensor labeled sensor2. If your sensor's name is 'IR', accessing the right
        value will look like this:

        value_from_sensor2 = IR.value2
    
    IRSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
        
'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

from grove.adc import ADC

class IRSensor(object):
    '''
    IR Sensor class

    Args:
        pin(int): number of the analog pin the sensor is connected to.
    '''
    def __init__(self, channel1, channel2):
        self.channel1 = channel1
        self.channel2 = channel2
        self.adc = ADC(address = 0x08)

    @property
    def value1(self):
        '''
        Get the infrared strength value, maximum value is 999

        Returns:
            (int): ratio, 0 - 999
        '''
        value = self.adc.read(self.channel1)
        return value

    @property
    def value2(self):
        '''
        Get the infrared strength value, maximum value is 999

        Returns:
            (int): ratio, 0 - 999
        '''
        value = self.adc.read(self.channel2)
        return value