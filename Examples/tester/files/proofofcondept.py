from stage import *
import cmdgui
import time

def examplefunction():
    
    stage2 = stage(title='TEST',width=60,height=15)
    cmdgui.setstage(stage2)

                #cmdgui.writeline(2,'This is a long message',stage2)
    for  i in range (1,6):
        if True:
                time.sleep(1)
        cmdgui.testwrite(str(i))
        #cmdgui.writeline(str(i))
        #cmdgui.setstage(stage(title=str(i),width=60,height=15))
