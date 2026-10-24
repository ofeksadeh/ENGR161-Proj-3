from basehat import IMUSensor
import time
import cmdgui

def IMU_Test():
        IMU = IMUSensor()

#         imustage = cmdgui.stage('IMU Test',60,15)
        print("IMU Test")
#         cmdgui.setstage(imustage)
        
        result = ['IMU_Test']

#         cmdgui.writeline(imustage,'IMU will Read for 5 seconds, spin it!',1)
        print("IMU will Read for 5 seconds, please move the imu around")
        
        zerovalue = True
        for i in range(10):

            accel_x,accel_y,accel_z = IMU.getAccel()
            gyro_x, gyro_y, gyro_z = IMU.getGyro()
            mag_x, mag_y, mag_z = IMU.getMag()
            if accel_x * accel_y * accel_z * gyro_x * gyro_y * gyro_z * mag_x * mag_y * mag_z != 0:
                zerovalue = False

            print(" AX = %7.2f m/s^2  AY = %7.2f m/s^2  AZ = %7.2f m/s^2" % (accel_x, accel_y, accel_z))
            print(" GX = %7.2f dps GY = %7.2f dps GZ = %7.2f dps" % (gyro_x, gyro_y, gyro_z))          
            print(" MX = %7.2f uT  MY = %7.2f uT  MZ = %7.2f uT" % (mag_x, mag_y, mag_z))
            print()
            
            time.sleep(0.5)

        if zerovalue:
#                 cmdgui.writeline(imustage,'ERROR: zero value detected',7)
                print("ERROR: zero value detected")
                print("IMU Test: FAILED")
                result.append('FAILED')
        else:
                print("Only non-zero values detected")
                print("IMU Test: Passed")
                result.append('PASSED')
#         cmdgui.writeline(imustage,str(result[0]+": " + result[1]),8)
        time.sleep(1)
        return(result)
