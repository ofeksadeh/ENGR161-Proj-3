import time
import cmdgui

def printresults(testresults):
        printresultstage = cmdgui.stage('Test Results',60,15)
        cmdgui.setstage(printresultstage)

        cmdgui.writeline(printresultstage,'Test Results:',1)

        for i in range(0,len(testresults)):
                cmdgui.writeline(printresultstage,str(testresults[i][0]+": " + testresults[i][1]),3+i)
        time.sleep(1)
        return()
