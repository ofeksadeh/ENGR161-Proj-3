# Encoder_Examples.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the buildhat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from buildhat import Motor
import time

def main():

    # set the port to be used
    # if sensor is plugged into port A, pin should be 'A'
    # make sure to only plug in the motors to motor ports of the Grove BuildHat ('A', 'B', 'C', 'D')
    port = 'A'

    # Initializing the motor so the functions within the class can be used
    print("Initiating BuildHAT and motors")
    print("this may take a while (~10 seconds)")
    motor = Motor(port)


    try: 
        while True:
            try: 
                # update and read the values of the motor
                speed = motor.get_speed()
                absPosition = motor.get_aposition()
                position = motor.get_position()

                # print values
                print("Motor speed: {}".format(speed))
                print("Absolute Position: {}".format(absPosition))
                print("Position: {}".format(position))

                time.sleep(.5)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()

