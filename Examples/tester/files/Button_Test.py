from basehat import Button  # Import the simplified Button class
import time
import cmdgui

#https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
def Button_Test():
        result = ['Button_Test']
        
        #bpmotorstage = cmdgui.stage(title = 'BrickPi Button Test',width = 60, height = 15)
        print("Button Test")
        #cmdgui.setstage(bpmotorstage)
        
        zerovalue = True

        pin = 5  #Assuming pin 5 for the Button
        button = Button(pin)  #Create a Button instance
        time.sleep(0.25)

        starttime = time.time()

        #cmdgui.writeline(bpmotorstage,'Press the button. Test will time out in 5 seconds.',1)
        print("Press the button. Test will time out in 5 seconds.")
        
        temp = 1
        
        while True:
                if (time.time() - starttime)>temp:
                        #cmdgui.writeline(bpmotorstage,"Timeout in %1d" % int(5 - (time.time() - starttime)),3)
                        print("Timeout in %1d" % round(5 - (time.time() - starttime)))
                        temp += 1

                if button.value == 1:
                        zerovalue = False
                        #cmdgui.writeline(bpmotorstage,'boop!',4)
                        print("boop")
                        break
                elif time.time() - starttime > 5:
                        #cmdgui.writeline(bpmotorstage,'Timed Out :(',4)
                        print("Time Out")
                        break

        if zerovalue:
                #cmdgui.writeline(bpmotorstage,"ERROR: zero value detected",6)
                print("ERROR: zero value detected")
                print("Button Test: FAILED")
                result.append('FAILED')
        else:
                #cmdgui.writeline(bpmotorstage,"Non-zero values returned, good!",6)
                print("Non-zero values returned")
                print("Button Test: PASSED")
                result.append('PASSED')
        #cmdgui.writeline(bpmotorstage,str(result[0]+": " + result[1]),7)
        time.sleep(1)
        return(result)
