import serial
from oomBase import *


########  Codes
"""
    M114    Report Position



"""

def getDict(x=None,y=None,z=None,rx=None,ry=None,rz=None):
    return {"X" : x,"Y" : y,"Z" : z,"RX" : rx,"RY" : ry,"RZ" : rz}

class machine:


##################################  BASIC HELPERS

    def __init__(self,port="COM6"):
        print("Starting Machine on port: " + port)
        self.ser = serial.Serial(
                port=port,
                baudrate=38400,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
        oomDelay(8)
        print(self.read())
        #self.ser.open()

    def close(self):
        print("    Closing Machine")
        self.ser.close()   

    def read(self):

        #return self.ser.read_all().decode("utf-8") 
        bytes("Waiting for input:"

    def sendString(self,st,debug=True,waitOk=False):
        if debug:
            print("        Sending: " + st)
            bts = bytes(st + "\n\r", encoding='utf8')
        self.ser.write(bts)
        oomDelay(1)
        if not waitOk:
            read = self.read()
            return read
        else:
            waitTry = 100
            for x in range(0,waitTry):
                read = self.read())
                print(read)
                if "Waiting for input" in read:
                    return read
                else:
                    oomDelay(1)

    def sendCommand(self, command,x=None,y=None,z=None,s=None,waitOk=False):
        #if command.startswith("M"):
        return self.sendString(command,waitOk=waitOk).replace("\n","")    


###################  Tests

    def testMachine(self):
        print("Testing Machine")
        #self.sendString("G1 X10")
        #print(self.read())        
        pos = {"X" : 0,"Y" : 0,"Z" : 30,"E" : 0,}
        test = self.move(pos,abs=True)
        print("Absolute Positioning: " + test)
        pos = {"X" : 30,"Y" : 30,"Z" : 0,"E" : 0,}
        test = self.move(pos)
        test = self.setRelativePositioning()
        print("Relative Positioning: " + test)
        pos = self.getPosition()        
        print("Get Position: " + str(pos))        
        pos = {"X" : 10,"Y" : 10,"Z" : 10,"E" : 0}
        test = self.move(pos)
        
        

##################################  SIMPLE GCODE


#####################  Movement

    def getPosition(self):
        ######  M114
        ######  X:0.00 Y:0.00 Z:0.00 E:0.00 Count X:0 Y:0 Z:0
        locString = self.sendCommand("C,",waitOk=True)        
        replaceList = []
        replaceList.append("X:")
        replaceList.append("Y:")
        replaceList.append("Z:")
        replaceList.append("E:")
        replaceList.append("Count:")
        for rep in replaceList:
            locString = locString.replace(rep,"")
        locList = locString.split(" ")        
        x=locList[0]
        y=locList[1]
        z=locList[2]
        e=locList[3]
        return {"X" : x,"Y" : y,"Z" : z,"E" : e,}

    def home(self,axis=""):
        command = "G28 " + axis
        print("    Homing...") 
        test = self.sendCommand(command,waitOk=True)
        if "ok" not in test:
            raise Exception("Error when homing") 
        return test          


    def move(self,pos=None,x=None,y=None,z=None,rx=None,ry=None,rz=None,feedrate=None,abs=False,wait=False):
        ##### Relative Setting
        if abs:
            self.setAbsolutePositioning()
        else:
            self.setRelativePositioning()

        #######  Sorting out coordinates
        if pos == None:
            pos = {"X" : x,"Y" : y,"Z" : z,"E" : e,}
        command = "G1"
        if pos["X"] != None:
            command = command + " X" + str(pos["X"] )
        if pos["Y"] != None:
            command = command + " Y" + str(pos["Y"]) 
        if pos["Z"] != None:
            command = command + " Z" + str(pos["Z"])
        if pos["E"] != None:
            command = command +" E" + str(pos["E"]   )
        if feedrate != None:
            command = command +" F" + feedrate  
        test = self.sendCommand(command)
        if "ok" not in test:
            raise Exception("Error when moving")        
        if wait:
            self.getPosition()            
        return test

############################# Positioning routines

    def setAbsPos(self):
        self.setAbsolutePositioning()

    def setAbsolutePositioning(self):
        command = "G90"
        test = self.sendCommand(command)
        if test != "ok":
            raise Exception("Error when setting absolute positioning") 
        return test       

    def setRelPos(self):
        self.setAbsolutePositioning()

    def setRelativePositioning(self):
        command = "G91"
        test = self.sendCommand(command)
        if test != "ok":
            raise Exception("Error when setting relative positioning")    
        return test            

    def setPosition(self,pos=None,x=None,y=None,z=None,e=None):
        if pos == None:
            pos = [x,y,z,e]
        command = "G92"
        if pos["X"] != None:
            command = command + " X" + str(pos["X"] )
        if pos["Y"] != None:
            command = command + " Y" + str(pos["Y"] )
        if pos["Z"] != None:
            command = command + " Z" + str(pos["Z"])
        if pos["E"] != None:
            command = command +" E" + str(pos["E"]   )
        test = self.sendCommand(command)
        if "ok" not in test:
            raise Exception("Error when setting position")    
        return test            


    

