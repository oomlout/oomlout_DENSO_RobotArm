import DENS_CodeCreate as dcc


points  = dcc.getDefaultPoints()
commands = []

programName = "TEST-PYTHON-001"

##dcc.newProject(programName)
dcc.newProgram(programName)


d = {
    "NAME" : "move100",
    "X" : 100,
    "Y" : 100,
    "Z" : 100,
    "AX" : 0,
    "AY" : 0,
    "AZ" : 0
}
points.append(d)
d = {
    "NAME" : "homeUp",
    "X" : 450,
    "Y" : 0,
    "Z" : 900,
    "AX" : 180,
    "AY" : 0,
    "AZ" : 180
}
points.append(d)



command = {"COMMAND" :      "MOVE",
            "MODIFIER" :    "L",
            "POINT1" :  "oomHome"}
commands.append(command)
command = {"COMMAND" :      "MOVE",
            "MODIFIER" :    "L",
            "POINT1" :  "homeUp"}
commands.append(command)



dcc.addPointsToProgram("TEST-PYTHON-001",points)

dcc.addCommandsToProgram(programName, commands)
