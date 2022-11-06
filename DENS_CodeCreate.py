from oomBase import *

def getPro1Name(name):
    return "programs/" + name + "/PRO1.pac"

def newProject(name):
    oomMakeDir(name)
    newDir = "programs/" + name + "/"
    oomCopyDir("programs/DENS-BLANK-01/",newDir)
    
    
def newProgram(name):
    contents = "" 
    contents = contents + "" + "\n"

    #contents = contents + "" + "\n"
    #contents = contents + '\'!TITLE "' + name + '"'  + "\n"
    contents = contents + 'PROGRAM PRO1'  + "\n"
    contents = contents + "" + "\n"
    contents = contents + "TakeArm 0 keep=0" + "\n"
    contents = contents + "MOTOR ON" + "\n\n"

    oomWriteToFile(getPro1Name(name),contents)



def getDefaultPoints():
    rv  =[]
    d = {
    "NAME" : "oomHome",
    "X" : 450,"Y" : 0,"Z" : 800,"AX" : 45,"AY" : 45,"AZ" : 45
    }
    rv.append(d)
    return rv

def addCommandsToProgram(name,commands):
    contents  ="*BEGIN:\n\n"
    for command in commands:
        c = getCommandString(command)
        contents = contents + c + "\n"



    contents  =contents + "GOTO *BEGIN" + "\n"
    oomAddLineToFile(getPro1Name(name),contents)



def getCommandString(command):
    rv = ""
    if command["COMMAND"] == "MOVE":
        rv = "MOVE " + command["MODIFIER"] + ", " + command["POINTNAME"]           
    elif command["COMMAND"] == "JOG":    
        j = command["POINT1"]
        moveString = "(" + str(j["X"]) + ","  +str(j["Y"]) + ","  +str(j["Z"]) + ","  +str(j["RX"]) + ","  +str(j["RY"]) + ","  +str(j["RZ"]) + ")"
        rv = rv + "temp1 = CURPOS + " + moveString + "\n"
        rv = rv + "MOVE P, temp1" 
    elif command["COMMAND"] == "DELAY":
        rv = "DELAY " + command["VALUE1"]
    return rv

def addPointsToProgram(name,points):
    if len(points) > 0:
        contents = ""
        pointNames = ""
        for p in points:
            pointNames = p["NAME"] + "," + pointNames
        pointNames = pointNames[0:len(pointNames)-1]
        pointDef = "DEFPOS temp1," + pointNames
        contents = contents + pointDef + "\n\n"

        pointDec = ""
        for p in points:
            pointline = p["NAME"] + " = (" + str(p["X"]) + "," + str(p["Y"]) + "," + str(p["Z"]) + "," + str(p["AX"]) + "," + str(p["AY"]) + "," + str(p["AZ"]) + ")"
            pointDec = pointDec + pointline + "\n" 
        contents = contents + pointDec






    oomAddLineToFile(getPro1Name(name),contents)