from buildhat import Motor
import time
import cmdgui

##PARAMETERS:
motor_run_time = 6 #seconds (approximate)


def Motor_Test():
        result = ['Motor_Test']
#         bpmotorstage = cmdgui.stage('BrickPi Motor Test',60,15)
        print("Motor Test")
#         cmdgui.setstage(bpmotorstage)

        zerovalue = False

#         cmdgui.writeline(bpmotorstage,"Activating Motor",1)
        print("Starting Motor")
        
        motor = Motor('A')
        motor.stop()
        motor.set_default_speed(80)

        prevenc = 0
        
        motor.start()
        for i in range (1, motor_run_time*2):
                time.sleep(0.5)
                encoder = motor.get_position()
#                 cmdgui.writeline(bpmotorstage,("Encoder A: %6d" % encoder),3)
                print("Encoder A: %6d" % encoder)
                if encoder == prevenc:
                        zerovalue = True
                prevenc = encoder
        motor.stop()

        if zerovalue:
#                 cmdgui.writeline(bpmotorstage,"ERROR: zero value detected",5)
                print("ERROR: zero value detected")
                print("Motor Test: FAILED")
                result.append('FAILED')
        else:
#                 cmdgui.writeline(bpmotorstage,"Non-zero values returned, good!",5)
                print("Motor Test: PASSED")
                result.append('PASSED')
                                 
#         cmdgui.writeline(bpmotorstage,str(result[0]+": " + result[1]),7)
        motor.stop()
        time.sleep(1)
        return(result)
