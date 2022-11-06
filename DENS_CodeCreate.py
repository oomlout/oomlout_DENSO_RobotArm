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

    oomWriteToFile(getPro1Name(name),contents)



def getDefaultPoints():
    rv  =[]
    d = {
    "NAME" : "oomHome",
    "X" : 450,
    "Y" : 0,
    "Z" : 800,
    "AX" : 180,
    "AY" : 0,
    "AZ" : 180
    }
    rv.append(d)
    return rv

def addCommandsToProgram(name,commands):
    contents  =""
    for command in commands:
        c = getCommandString(command)
        contents = contents + c + "\n"

    oomAddLineToFile(getPro1Name(name),contents)


def getCommandString(command):
    rv = ""
    if command["COMMAND"] == "MOVE":
        rv = "MOVE " + command["MODIFIER"] + " @P " + command["POINT1"]
    return rv

def addPointsToProgram(name,points):
    if len(points) > 0:
        contents = ""
        pointNames = ""
        for p in points:
            pointNames = p["NAME"] + "," + pointNames
        pointNames = pointNames[0:len(pointNames)-1]
        pointDef = "DEFPOS " + pointNames
        contents = contents + pointDef + "\n\n"

        pointDec = ""
        for p in points:
            pointline = p["NAME"] + " = (" + str(p["X"]) + "," + str(p["Y"]) + "," + str(p["Z"]) + "," + str(p["AX"]) + "," + str(p["AY"]) + "," + str(p["AZ"]) + ")"
            pointDec = pointDec + pointline + "\n" 
        contents = contents + pointDec






    oomAddLineToFile(getPro1Name(name),contents)