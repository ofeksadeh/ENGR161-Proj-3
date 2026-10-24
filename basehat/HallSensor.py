# HallSensor.py

# Created by Owen Bishop on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
Hall Sensor:
    Description:
        This sensor has only one value that can be accessed: a digital value of either 0 or 1 that is 
        dependent on the strength of magnetic field present at the sensor. The sensor outputs a 1 when 
        a strong magnetic field is detected

    Hardware:
        The hall sensor connects to digital pins on the Grove BaseHAT (any port starting with a D)
        Initialize the sensor using only the number of the port (do not include the D)
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Hall_Sensor/


    Initialization:

        sensor_name = HallSensor(pin)

        If you plug your Hall Sensor into D5 and want to name it 'Hall', your initialization will
        look like this:

        Hall = HallSensor(5)
    
    HallSensor.value:
        Read the value from the sensor. If your sensor's name is 'Hall', accessing the value will
        look like this:

        value_from_sensor = Hall.value
        
    
    HallSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
        
'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

from gpiozero import DigitalInputDevice
from gpiozero import HoldMixIn

class HallSensor(HoldMixin, DigitalInputDevice):
    """
    Simple Hall Sensor Class

    Args:
        pin(int): the digital pin to which the sensor is assigned
        pull_up(bool): whether the sensor is set to pull up or down. This impacts whether the 
            sensor returns a 0 or 1 when near a magnet and must be set to false for the wiring 
            setup of the base hat.
        bounce_time(float): The length of time (in seconds) after the button is presse during which 
            new inputs are ignored. This minimizeds 'bouncy' signals, where the output of the button
            changes rapidly as it is being pressed. The base time for this is 1 second.
   
    """
    def __init__(self, pin=None, *, pull_up=True, active_state=None,
                 bounce_time=None, pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            bounce_time=bounce_time, pin_factory=pin_factory)

    @property
    def value(self):
        """
        Returns 1 if the button is currently pressed, and 0 if it is not.
        """
        return super().value
