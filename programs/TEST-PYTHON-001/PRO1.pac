
PROGRAM PRO1

TakeArm 0 keep=0
MOTOR ON

DEFPOS temp1,homeUp,move100,oomHome

oomHome = (450,0,800,45,45,45)
move100 = (100,100,100,0,0,0)
homeUp = (450,0,900,45,45,45)

*BEGIN:

MOVE L, oomHome
MOVE L, homeUp
temp1 = CURPOS + (100,0,0,20,20,20)
MOVE P, temp1
DELAY 3000 
GOTO *BEGIN


