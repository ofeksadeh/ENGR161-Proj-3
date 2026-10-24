from sys import stdout as out
import stage

#https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html

csclear = '\033[2J'
csorigin = '\033[0;0H'
csnext = '033[1B'
csprev = '033[1E'
csclearline = '\033[K'

class stage:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.hline = '=' * width + '\n'
        self.rowstr = '*' + ' ' * (width - 2) +  ('*\n')
        self.titlestr = '*' + ' ' * ((int(width / 2) - int(len(title)/2)) - 1) + title + ' ' * (width - (int(width / 2) - int(len(title)/2)) - 1 - len(title)) + '*\n'

def writeline(stage,message,row):
    out.write(csorigin)
    out.write('\033[' + str(row+4) + ';0f')
    out.write(csclearline)
    out.write(stage.rowstr)
    out.write('\033[' + str(row+4) + ';3f')
    out.write(message + '\r')
    out.write('\033[' +str(stage.height+1) + ';0H')
    return

def setstage(stage):
    out.write(csclear)
    out.write(csorigin)

    out.write(stage.hline)
    out.write(stage.titlestr)
    out.write(stage.hline)

    for i in range(0,stage.height - 4):
        out.write(stage.rowstr)
    out.write(stage.hline)
    return
