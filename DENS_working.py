from oomBase import *
import DENS
import serial
import serial.tools.list_ports


######  Basics
machine = DENS.machine()
#machine.testMachine()
#print(machine.sendCommand("M114"))
posA = machine.getPosition()
print(posA)
#oomDelay(2)

posA["X"] = posA["X"] + 10
#machine.move(posA,abs=True)

moveA = {'X': -10, 'Y': 0, 'Z': 0, 'RX': 0, 'RY': 0, 'RZ': 0}
#machine.move(moveA,abs=False)



jog = 2

movements = {}

movements["up"] = ["X", jog]
movements["down"] = ["X", -jog]
movements["left"] = ["Y", jog]
movements["right"] = ["Y", -jog]
movements["-"] = ["Z", -jog]
movements["+"] = ["Z", jog]

movements["a"] = ["RX", jog]
movements["d"] = ["RX", -jog]
movements["w"] = ["RY", jog]
movements["s"] = ["RY", -jog]
movements["q"] = ["RZ", -jog]
movements["z"] = ["RZ", -jog]

import keyboard

print("Waiting for input")
while True:
    for movement in movements:        
        if keyboard.is_pressed(movement):
            moveA[movements[movement][0]] = movements[movement][1]
    machine.move(moveA,abs=False)
    moveA = {'X': 0, 'Y': 0, 'Z': 0, 'RX': 0, 'RY': 0, 'RZ': 0}        

    
machine.close()

######  Serial port stuff
#ports = serial.tools.list_ports.comports()
#print(ports[0])

