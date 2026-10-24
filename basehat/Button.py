# Button.py

# Created by Aayush Iyengar on behalf on the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###
'''
Button:
    Description:
        This is a very simple sensor, representing whether the button has been pressed or not 
        using a digital output, with a 1 denoting the button being pressed and a 0 representing 
        it being unpressed. Functions can also be used to determine not only the state of the button
        but also when the button is pressed or released.

    Hardware:
        The button connects to digital pins on the Grove BaseHAT (any port starting with a D)
        Initialize the sensor using only the number of the port (do not include the D)
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Button/ 
    
    Initialization:
        button_name = Button(pin)

        If you plug your button into D5 and want to name it 'button' your initialization will
        look like this:

        button = Button(5)

    Button.value:
        Read the value of the button, returning a 1 if pressed and a 0 if not. If your button's 
        name is 'button', accessing this value will look like this:

        value_from_button = button.value

    Button.is_pressed:
        Returns whether the button is currently pressed as a boolean. If your button's name is
        'button', accessing this value will look like this:

        is_button_pressed = button.is_pressed
    
    Button.pressed_time:
        Returns the total length of time for which the butten has been pressed, or 'None' if it
        is not currently pressed. If your button's name is 'button', accessing this value will 
        look like this:

        press_length = button.pressed_time

    Button.when_pressed:
        This parameter stores a function that will automatically be run upon the button being
        pressed. If your button's name is 'button' and you want the function 'on_press()' to 
        be run each time it is pressed, assigning this would look like this:

        button.when_pressed = on_press

        An example of this being used can be seen in Button_Example.py

    Button.when_released:
        This parameter stores a function that will automatically be run upon the button being
        released. If your button's name is 'button' and you want the function 'on_release()' to 
        be run each time it is released, assigning this would look like this:

        button.when_released = on_release

        An example of this being used can be seen in Button_Example.py
    
    Button.wait_for_press():
        This function will pause the code that is running until the button is pressed. If your 
        button's name is 'button', employing this funciton would look like this:

        button.wait_for_press()

    Button.wait_for_release():
        This function will pause the code that is running until the button is released. If your 
        button's name is 'button', employing this funciton would look like this:

        button.wait_for_release()
    
    Button_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
'''

from gpiozero import DigitalInputDevice
from gpiozero import HoldMixIn

class Button(HoldMixin, DigitalInputDevice):
    """
    Simple Button Class

    Args:
        pin(int): the digital pin to which the button is assigned
        pull_up(bool): whether the button is set to pull up or down. This impacts whether the 
            button returns a 0 or 1 when pressed and must be set to false for the wiring setup of 
            the base hat.
        bounce_time(float): The length of time (in seconds) after the button is presse during which 
            new inputs are ignored. This minimizeds 'bouncy' signals, where the output of the button
            changes rapidly as it is being pressed. The base time for this is 1 second.
   
    """
    def __init__(self, pin=None, *, pull_up=True, active_state=None,
                 bounce_time=None, hold_time=1, hold_repeat=False,
                 pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            bounce_time=bounce_time, pin_factory=pin_factory)
        self.hold_time = hold_time
        self.hold_repeat = hold_repeat

    @property
    def value(self):
        """
        Returns 1 if the button is currently pressed, and 0 if it is not.
        """
        return super().value



Button.is_pressed = Button.is_active
Button.pressed_time = Button.active_time
Button.when_pressed = Button.when_activated
Button.when_released = Button.when_deactivated
Button.wait_for_press = Button.wait_for_active
Button.wait_for_release = Button.wait_for_inactive