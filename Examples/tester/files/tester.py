#No line sensors - DONE
#Add IR sensor
#Change motor duration - DONE (note this is applied in the BPMotor_Test.py file and as such applies to the V1 testfile too)

import basehat
import buildhat
import sys
import time

import cmdgui
from IMU_Test import *
from Ultrasonic_Test import *
from Button_Test import *
from Motor_Test import *
from IR_Test import *
from printresults import *

if __name__ == "__main__":
        try:
            #plug the IMU into I2C, Ultrasonic into D22, IR into A0, Button into D5, and motor into port A
                testresults = []
                testresults.append(IMU_Test())
                testresults.append(Ultrasonic_Test())
                testresults.append(IR_Test())
                testresults.append(Button_Test())
                testresults.append(Motor_Test())
                motor = Motor('A')
                motor.stop()
                print("\nTest Results:")
                for result in testresults:
                    time.sleep(.5)
                    result = list(result)
                    print(f"{result[0]}: {result[1]}")


        except KeyboardInterrupt:
                sys.exit()

