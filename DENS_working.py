from oomBase import *
import DENS
import serial
import serial.tools.list_ports


######  Basics
machine = DENS.machine()
#machine.testMachine()
#print(machine.sendCommand("M114"))
print(machine.getPosition())
#oomDelay(2)
machine.close()


######  Serial port stuff
#ports = serial.tools.list_ports.comports()
#print(ports[0])

pass