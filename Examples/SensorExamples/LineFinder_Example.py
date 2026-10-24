# LineFinder_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

from basehat import LineFinder
import time

def main():

    # set the pin to be used
    # if sensor is plugged into port D5, pin1 should be 5
    # make sure to only plug in LineFinder Sensor to digital ports of the Grove BaseHAT (D5, D16, D18, D22, D24, D26)
    pin = 5

    # Initializing the sensor so the function within the class can be used
    lineFinder = LineFinder(pin)

    try: 
        while True:
            try: 
                # update and read the values of the lineFinder
                curValue = lineFinder.value

                # print values
                print("LineFinder value: {}".format(curValue))

                time.sleep(0.5)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
