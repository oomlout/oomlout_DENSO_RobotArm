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

    def __init__(self,port="COM9"):
        print("Starting Machine on port: " + port)
        self.ser = serial.Serial(
                port=port,
                baudrate=38400,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
        #print(self.read())
        #self.ser.open()

    def close(self):
        print("    Closing Machine")
        self.ser.close()   

    def read(self):
        return self.ser.read_all().decode("utf-8") 
        #return self.ser.read(500).decode("utf-8") 
        

    def sendString(self,st,debug=True):
        self.ser.flushInput()
        if debug:
            print("        Sending: " + st)
            st = st + "\r"
        self.ser.write(st.encode())
        waitTry = 50
        for x in range(0,waitTry):
            read = self.read()
            #print("read" + read)
            if "OK" in read:
                return read
            else:
                if "ERROR" in read:
                    raise Exception("Error in command (Response)")
                oomDelay(0.1)
        raise Exception("Error in command (Timeout)")

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
        pos = self.sendString("G")
        pos = pos.split("\r")[0]
        positions = pos.split(" ")
        points = ["X","Y","Z","RX","RY","RZ"]
        rv = {}
        for i in range(0,6):
            rv[points[i]] = float(positions[i])
        return rv

    def move(self,pos=None,speed=None,abs=False):
        ##### Relative Setting
        command = "M" ### default to a relative move
        if abs:
            command = "P" ### make it an acsolut move
        fullCommand = command + ","
        for p in pos:
            fullCommand = fullCommand + str(pos[p]) + ","
        self.sendString(fullCommand)
        
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


    

