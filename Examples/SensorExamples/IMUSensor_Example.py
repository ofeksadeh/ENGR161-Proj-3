# IMUSensor_Example.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import IMUSensor
import time

def main():
    print("running")
    # Initializing the IMU so the example can utilize the sensor
    IMU = IMUSensor()
    
    try: 
        while True:
            try:
                # Reading acceleration values and printing them
                x, y, z = IMU.getAccel()
                print(" AX = %7.2f m/s^2  AY = %7.2f m/s^2  AZ = %7.2f m/s^2" % (x, y, z))

                # Reading gyroscope values and printing them
                x, y, z = IMU.getGyro()
                print(" GX = %7.2f dps GY = %7.2f dps GZ = %7.2f dps" % (x, y, z))          

                # Reading magnet values and printing them
                x, y, z = IMU.getMag()
                print(" MX = %7.2f uT  MY = %7.2f uT  MZ = %7.2f uT" % (x, y, z))     

                # Waiting 1 second until new sensor readings   
                time.sleep(1.0)
                print("yummy")
            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
