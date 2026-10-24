# Run_Examples.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the buildhat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
import time
from buildhat import Motor

def main():
    
    # set the pin to be used
    # if sensor is plugged into port A, pin should be 'A'
    # make sure to only plug in the motors to motor ports of the Grove BuildHat ('A', 'B', 'C', 'D')
    print("Initiating BuildHAT and motors")
    print("this may take a while (~10 seconds)")
    motor = Motor('B')

    # uncomment to use Motor B
    # motorB = Motor('B')

    # Function to print the current speed, position and absolute position of the motors
    def handle_motor(speed, pos, apos):
        """Motor data

        :param speed: Speed of motor
        :param pos: Position of motor
        :param apos: Absolute position of motor
        """
        print("Motor", speed, pos, apos)

    try: 
        while True:
            try:
                # Any of these two to five line blocks can be uncommented to test and play with the functionality
                # of the various motor functions that are available with the motors
                print("Motor Testing")

                # Leave these lines uncommented because they print the current speed, position and absolute position
                # of the motors and set the default speed
                # motor.when_rotated = handle_motor
                
                motor.set_default_speed(50)

                # manual_run_for_time(motor)

                # run_for_time(motor)

                run_360_cycle(motor)

                # run_some_rotations(motor)

                # run_between_positions(motor)

                # Make sure to connect a second motor and uncomment line 22
                # run_two_motors(motor, motorB)

                


            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
        motor.stop()
        try:
            motorB.stop()
        except:
            pass



def manual_run_for_time(motor):
    print("Start motor")
    motor.pwm(.5)
    time.sleep(3)
    print("Stop motor")
    motor.pwm(0)
    time.sleep(1)

def run_for_time(motor):
    print("Run for seconds: 5")
    motor.run_for_seconds(5)
    time.sleep(3)

def run_360_cycle(motor):
    print("Run for degrees 360")
    motor.run_for_degrees(360)
    time.sleep(3)

    print("Run for degrees -360")
    motor.run_for_degrees(-360)
    time.sleep(3)

def run_some_rotations(motor):
    print("Run for rotations: 2")
    motor.run_for_rotations(2)
    time.sleep(3)

def run_between_positions(motor):
    print("Run to position -90")
    motor.run_to_position(-90)
    time.sleep(3)

    print("Run to position 90")
    motor.run_to_position(90)
    time.sleep(3)

def run_two_motors(motor, motorB):
    print("Run both")
    motor.run_for_seconds(5, blocking=False)
    motorB.run_for_seconds(5, blocking=True)
    time.sleep(5)

if __name__ == '__main__':
    main()
