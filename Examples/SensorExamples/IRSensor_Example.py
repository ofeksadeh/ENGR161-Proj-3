# IRSensor_Example.py

# Created by Seth McConkey on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import IRSensor
import time

def main():

    # set the pin to be used
    # if sensor is plugged into port A0, pin1 should be 0 and pin2 should be 1
    # make sure to only plug in IR Sensor to analog ports of the Grove BaseHAT (A0, A2, A4, A6)
    pin1 = 0
    pin2 = pin1 + 1

    # initialize the sensor by naming the class instance and setting the pins to use
    # 'IR' is the name of the instance, pin1 and pin2 are the pins being used
    IR = IRSensor(pin1, pin2)

    print('Detecting infrared...')

    try: 
        while True:
            try: 
                # update and read the values of the left and right infrared sensors
                value1 = IR.value1
                value2 = IR.value2

                # print values
                print("IR value1: {}   IR value2: {}".format(value1, value2))

                time.sleep(0.5)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
            
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
