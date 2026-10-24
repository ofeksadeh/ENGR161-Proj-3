### DO NOT MODIFY CODE IN THIS FILE ###
### THIS CODE IS NOT RELEVENT TO 16X STUDENTS ###
# [Name of Module]

# Created by [your name] on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
[Sensor/Motor Name]:
    Description:
        Description of Sensor/Motor

    Hardware:
        What port to connect to (analog, digital, i2c, BuildHAT motor port, etc)
        
        More info:
        Link to HAT webpage (either BuildHAT for motors or Grove BaseHAT for sensors)
        Link to information webpage on seeedstudio website (search [sensor name] grove on Google)
    
    Initialization:
        Description on how to initialize sensor/motor

    [Function/Property Name]:
        Description of function/property and how to use (include basic syntax for calling
            function in another program)

    [Function/Property #2 Name]:
        Description of function/property and how to use (include basic syntax for calling
            function in another program)
    
    [Example File]: 
        Name of Example File Where Sensor/Motor is Intialized and Demonstrated

'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

# import statements

# for LightSensor, follow this code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_light_sensor_v1_2.py

# for UltrasonicSensor, follow this code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_ultrasonic_ranger.py

# for LineFinder, follow this code (search for LineSensor):
# https://github.com/gpiozero/gpiozero/blobs/master/gpiozero/input_devices.py

# for Button, follow this code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_button.py

# for IMU, follow this code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_imu_9dof_icm20600_ak09918.py

# For most of these, you will simply just need to rename the class to make the name simpler.
# You may change property namees/functions to be more consistent or easier to remember, but 
# that is not 100% necessary all the time.
# If you are confused on how the class works, consider changing it to be more intuitive
# so it is also easier for students

class ClassName(object):
    '''
    ClassName class

    Args:
    '''
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    @property
    def value(self):
        '''
        Description

        Returns:
        '''
        return value

    def function(self, parameter1, parameter2):
         '''
        Description

        Returns:
        '''
        return

