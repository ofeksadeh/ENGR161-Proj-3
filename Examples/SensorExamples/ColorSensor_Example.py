# Run_Examples.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the buildhat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
import time
from buildhat import ColorSensor

def main():

    # set the port to be used
    port = 'A'

    # Initializing the sensor so the function within the class can be used
    color = ColorSensor(port)

    try: 
        while True:
            try:
                # Getting the color in front of the sensor
                color_string = color.get_color()
                r, g, b, i = color.get_color_rgbi()

                # Printing the current reading and waiting to take another reading for 1 second
                print('color: {}'.format(color_string))
                print('r g b i: {}, {}, {}, {}'.format(r, g, b, i))
                time.sleep(1)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
        

if __name__ == '__main__':
    main()
