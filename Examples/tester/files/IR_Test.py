from basehat import IRSensor
import time
import cmdgui


#PARAMETERS:
range_low = 1 #Minimum range between lowest value and highest value for pass. Adjust if needed.
range_high = 100 #Maximum range between lowest value and highest value for pass. Adjust if needed.

#NOTE: the above value is based on the understanding that 0-1023 is the range of output.


def IR_Test():
        result = ['IR_Test']

#         IRStage = cmdgui.stage(title = 'GroveIR_Test',width = 60, height = 15)
        print("IR Test")
#         cmdgui.setstage(IRStage)

#         cmdgui.writeline(IRStage,'IR will read for 5s, cover up sensors with you hand then point at IR!',1)

        minVals = [100000, 100000] #very high values, exact values don't matter
        maxVals = [0, 0]

        pin1 = 0
        pin2 = pin1 + 1

        # initialize the sensor by naming the class instance and setting the pins to use
        # 'IR' is the name of the instance, pin1 and pin2 are the pins being used
        IR = IRSensor(pin1, pin2)

        for i in range(20):
            readval = [IR.value1, IR.value2]

            for i in range(2):
                if readval[i] < minVals[i]:
                    minVals[i] = readval[i]
                if readval[i] > maxVals[i]:
                    maxVals[i] = readval[i]

#             cmdgui.writeline(IRStage,'IR 1: '+ str(readval[0]) + 'IR 2: '+ str(readval[1]),3)
                print("IR value1: {}   IR value2: {}".format(readval[0], readval[1]))
            
            time.sleep(0.25)
            
        sen1fail = (maxVals[0]-minVals[0] < range_low) or (maxVals[0]-minVals[0] > range_high)
        sen2fail = (maxVals[1]-minVals[1] < range_low) or (maxVals[1]-minVals[1] > range_high)

        if (sen1fail) or (sen2fail):
#                 cmdgui.writeline(IRStage,'ERROR: Neither IR sensor is working.',5)
                print('IR Test: FAILED')
                result.append('FAILED')

        else:
                print('IR Test: PASSED')
                result.append('PASSED')
#         cmdgui.writeline(IRStage,str(result[0]+": " + result[1]),6)
        time.sleep(1)
        return(result)
