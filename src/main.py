import time
from buildhat import Motor
from basehat import UltrasonicSensor
from basehat import LightSensor

# ULTRASONIC_SENSOR_PIN = 5  # Pin for the ultrasonic sensor
# LIGHT_SENSOR_RIGHT_PIN = 0 #Pin for the right light sensor
# LIGHT_SENSOR_LEFT_PIN = 2 #Pin for the left light sensor
REAR_LEFT_MOTOR_PIN = 'A' #Pin for the rear left motor
REAR_RIGHT_MOTOR_PIN = 'B' #Pin for the rear right motor
FRONT_MOTOR_PIN = 'C' #Pin for the front motor
PATH_DARKNESS = 300 #Value treshold for detecting path using light sensors


def main():
    rearLeftMotor = Motor(REAR_LEFT_MOTOR_PIN)
    rearRightMotor = Motor(REAR_RIGHT_MOTOR_PIN)
    frontMotor = Motor(FRONT_MOTOR_PIN)
    # ultra = UltrasonicSensor(ULTRASONIC_SENSOR_PIN)
    # lightSenRight = LightSensor(LIGHT_SENSOR_RIGHT_PIN)
    # lightSenLeft = LightSensor(LIGHT_SENSOR_LEFT_PIN)

    setDefaultSpeed(rearLeftMotor, rearRightMotor, frontMotor, 50)
    try:
        while True:
            try:
                lightRight = lightSenRight.light
                # lightLeft = lightSenLeft.light
                # distance = ultra.getDist

                # while(lightRight <= PATH_DARKNESS or lightLeft <= PATH_DARKNESS):
                #     if(lightRight < PATH_DARKNESS and lightLeft >= PATH_DARKNESS):
                #         rearLeftMotor.run_for_rotations(2)
                #     elif(lightRight >= PATH_DARKNESS and lightLeft < PATH_DARKNESS):
                #         rearRightMotor.run_for_rotations(2)

                runMotors(rearLeftMotor, rearRightMotor, frontMotor)

                time.sleep(0.1)

            except IOError:
                print ("\nError occurred while attempting to read values")
                break
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")


def setDefaultSpeed(motor1, motor2, motor3, speed):
    """Set the default speed for three motors

    :param motor1: First motor
    :param motor2: Second motor
    :param motor3: Third motor
    :param speed: Speed to set for the motors
    """
    motor1.set_default_speed(speed)
    motor2.set_default_speed-(speed)
    motor3.set_default_speed(-speed)

def runMotors(m1, m2, m3):
    """Run three motors at the default speed

    :param m1: First motor
    :param m2: Second motor
    :param m3: Third motor
    """
    m1.run()
    m2.run()
    m3.run()
