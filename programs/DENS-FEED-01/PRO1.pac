PROGRAM PRO1
TakeArm 0 keep=0
MOTOR ON
PRINT "******************************"
PRINT "******  Starting DENS-FEED-01 PROGRAM"
PRINT "******************************"


'PRINT "          		P -- Goto Point (XYZaXaYaZ)                     P,x,y,z,ax,ay,az"
'PRINT "          		M -- Move (XYZ)                                 M,x,y,z,ax,ay,az"
'PRINT "          		J -- Move (joints to angles)                    J,J1,J2,J3,J4,J5,J6"
'PRINT "          		K -- Move (joints by angles)                    K,J1,J2,J3,J4,J5,J6"
'PRINT "          		G -- Print current position
'PRINT "          		Z -- No operation

'variable definition
DEFSTR strMode, strX, strY, strZ, strAX, strAY, strAZ, strExtra1, strExtra2, strExtra3, strExtra4

DEFSNG pX, pY, pZ, pAX, pAY, pAZ

DEFSTR nA

DEFSTR strInput

DEFINT arrSize = 50
DIM arrName(50) AS STRING
DIM arrX(50) AS SINGLE
DIM arrY(50) AS SINGLE
DIM arrZ(50) AS SINGLE
DIM arrAx(50) AS SINGLE
DIM arrAy(50) AS SINGLE
DIM arrAz(50) AS SINGLE



DEFINT working = 0
arrName(working) = "HOME"
arrX(working) = 450
arrY(working) = 0
arrZ(working) = 800
arrAx(working) = 180
arrAy(working) = 0
arrAz(working) = 180

FLUSH #2

*BEGIN:
LINEINPUT strInput
strInput = strInput + ",,,,,,,,,,,,,,,,"
 
strMode = LEFT(strInput, STRPOS(strInput, ",")-1)
strMode = RIGHT(strMode,1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))

'PRINT "  Mode: " + strMode
'PRINT "  Remaining: " + strInput
 
strX = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "  X: " + strX
'PRINT "  Remaining: " + strInput
 
strY = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "  Y: " + strY
'PRINT "  Remaining: " + strInput
 
strZ = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "  Z: " + strZ
'PRINT "  Remaining: " + strInput
 
strAX = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "  AX: " + strAX
'PRINT "  Remaining: " + strInput
	 
strAY = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "  AY: " + strAY
'PRINT "  Remaining: " + strInput
	 
strAZ = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))

strExtra1 = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))

strExtra2 = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))

strExtra3 = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))

strExtra4 = LEFT(strInput, STRPOS(strInput, ",")-1)
strInput = RIGHT(strInput, LEN(strInput)-STRPOS(strInput, ","))
'PRINT "       PARSED LINE    Mode: " + strMode + "  X: " + strX + "  Y: " + strY + "  Z: " + strZ + "  AX: " + strAX + "  AY: " + strAY + "  AZ: " + strAZ + "  X1: " + strExtra1 + "  X2: " + strExtra2 + "  x3: " + strExtra3 + "  X4: " + strExtra4

	 
pX = VAL(strX)
pY = VAL(strY)
pZ = VAL(strZ)
pAX = VAL(strAX)
pAY = VAL(strAY)
pAZ = VAL(strAZ)	


DEFPOS point2
DEFPOS point3
DIM xLoop AS INTEGER


SELECT CASE strMode
  CASE "P"
    'PRINT "P Mode (moving to point)"
    point2 = (pX,pY,pZ,pAX,pAY,pAZ)
    MOVE L, @P point2
    PRINT "OK"
  CASE "J" 'Move to a set position defining joint angles
	  'PRINT "J Mode (moving joints to angles)"
	  DRIVEA (1,pX),(2,pY),(3,pZ),(4,pAx),(5,pAy),(6,pAZ) 
    PRINT "OK"
  CASE "K" 'Move to a set position defining joint angles
	  'PRINT "K Mode (moving joints to angles relative)"
	  DRIVE (1,pX),(2,pY),(3,pZ),(4,pAx),(5,pAy),(6,pAZ) 
    PRINT "OK"
  CASE "M"
    'PRINT "M Mode (move relative)"
    point3 = (pX,pY,pZ)
    MOVE L, P0+(pX,pY,pZ,pAx,pAy,pAz)
    PRINT "OK"
  CASE "G"
    PRINT CURPOS			
    PRINT "OK"
  CASE "Z"
    PRINT "OK"
  CASE ELSE
    PRINT "ERROR"
END SELECT
GOTO *BEGIN

