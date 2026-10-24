# LightSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import LightSensor
import time

def main():
    # set the pin to be used
    # if sensor is plugged into port A0, pin1 should be 0 and pin2 should be 1
    # make sure to only plug in Light Sensor to analog ports of the Grove BaseHAT (A0, A2, A4, A6)
    pin = 0

    # initialize the sensor by naming the class instance and setting the pins to use
    lightSen = LightSensor(pin)
    try:
        while True:
            try:
                # update and read the value of the light sensor
                lightVal = lightSen.light

                # print current value and wait one second to read another value
                print('Light value: {0}'.format(lightVal))
                time.sleep(1)
            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
            
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")


if __name__ == '__main__':
    main()
