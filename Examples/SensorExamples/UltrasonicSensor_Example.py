# UltrasonicSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import UltrasonicSensor
import time

def main():

    # set the pin to be used
    # if sensor is plugged into port D5, pin1 should be 5
    # make sure to only plug in Ultrasonic Sensor to digital ports of the Grove BaseHAT (D5, D16, D18, D22, D24, D26)
    pin = 5

    # Initializing the sensor so the function within the class can be used
    ultra = UltrasonicSensor(pin)

    try: 
        while True:
            try:
                # Getting the current distance value from the ultrasonic sensor
                value = ultra.getDist

                # Printing the current reading and waiting to take another reading for 1 second
                print('{} cm'.format(value))
                time.sleep(1)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
        

if __name__ == '__main__':
    main()
