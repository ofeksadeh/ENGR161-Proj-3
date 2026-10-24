# LineFinder.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''

Grove Line Finder:
    Description:
        This sensor outputs whether it is being pointed at a black surface or a white surface,
        representing this digitally as a 0 for black or a 1 for white. The threshold for 
        determining this can be adjusted using a small screwdrive. This can be used to determine
        whether or not the sensor is over a line.

    Hardware:
        The line finder connects to digital pins on the Grove BaseHAT (any port starting with a D)
        Initialize the sensor using only the number of the port (do not includ the D)

        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Line_Finder/
    
    Initialization:
       sensor_name = LineFinder(pin)

        If you plug your line finder into D5 and want to name it 'lineFinder', your initialization 
        will look like this:

        lineFinder = LineFinder(5)

    LineFinder.value:
        Returns a 1 when the sensor is over something white and 0 when it is over something black.
        If your sensor's name is 'lineFinder', accessing this value will look like this:
       
         value_from_finder = lineFinder.value

    LineFinder.line_detected:
        Returns False when the sensor is over something white and True when it is over something black.        
        If your sensor's name is 'lineFinder', accessing this value will look like this:

        is_line = lineFinder.line_detected
    

    LineFinder_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.

'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

from gpiozero import SmoothedInputDevice

class LineFinder(SmoothedInputDevice):
    """
    Simple Line Finder Class

    Args:
        pin(int): the digital pin to which the line finder is assigned
        pull_up(bool): whether the button is set to pull up or down. This impacts whether the 
            button returns a 0 or 1 when pressed and must be set to false for the wiring setup of 
            the base hat.
        sample_rate(float): The number of values to read from the device per second. Defaults to 100.

    """
    def __init__(self, pin=None, *, pull_up=False, active_state=None,
                 queue_len=1, sample_rate=100, threshold=0.5, partial=False,
                 pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            threshold=threshold, queue_len=queue_len,
            sample_wait=1 / sample_rate, partial=partial,
            pin_factory=pin_factory)
        self._queue.start()


    # Gets the current reading whether there it detects black or white (0 or 1)
    @property
    def value(self):
        """
        Returns a value representing the average of the queued values. This
        is 0 for black under the sensor, and 1 for white under
        the sensor.
        """
        return super().value

    @property
    def line_detected(self):
        return not self.is_active