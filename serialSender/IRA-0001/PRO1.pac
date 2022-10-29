PROGRAM PRO1
TakeArm 0 keep=0
MOTOR ON
PRINT " "
PRINT " "
PRINT " "
PRINT " "
PRINT "******************************"
PRINT "******  Starting XXSERIALTEST PROGRAM"
PRINT "******************************"


'variable definition
DEFSTR strMode, strX, strY, strZ, strAX, strAY, strAZ, strExtra1, strExtra2, strExtra3, strExtra4

DEFSNG pX, pY, pZ, pAX, pAY, pAZ

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

working = 1
arrName(working) = "TEST"
arrX(working) = 550
arrY(working) = 100
arrZ(working) = 900
arrAx(working) = 180
arrAy(working) = 0
arrAz(working) = 180

working = 2
arrName(working) = "CALSET"
arrX(working) = -152.59
arrY(working) = 33.80
arrZ(working) = 762.06
arrAx(working) = 42.19
arrAy(working) = 3.08
arrAz(working) = 83.05

working = 3
arrName(working) = "CALSETL"
arrX(working) = -449.9
arrY(working) = 0.3837
arrZ(working) = 799.9833
arrAx(working) = -0.0033
arrAy(working) = -179.9856
arrAz(working) = 5

FLUSH #2
PRINT "    Input Goto Location (format x,y,z,ax,ay,az)"
PRINT "          FORMAT: Mode, x, y, z, ax, ay, az"
PRINT "          MODES: P -- Point (x,y,z,ax,ay,az)"
PRINT "          		D -- PRINTS POINTS"
PRINT "          		P -- Goto Point (XYZaXaYaZ)                     P,x,y,z,ax,ay,az"
PRINT "          		Q -- Goto Point in array (name)                 Q,x,y,z,ax,ay,az,name"
PRINT "          		R -- Add point to array (XYZaXaYaZ)             R,name"
PRINT "          		S -- Add curtrent position to list (x = name)   S,name"
PRINT "          		M -- Move (XYZ)                                 M,x,y,z,ax,ay,az"
PRINT "          		J -- Move (joints to angles)                    J,J1,J2,J3,J4,J5,J6"
PRINT "          		K -- Move (joints by angles)                    K,J1,J2,J3,J4,J5,J6"







*BEGIN:
PRINT "    Waiting for input:"
LINEINPUT strInput
strInput = strInput + ",,,,,,,,,,,,,,,,"
 
'PRINT "    Input String: " + strInput
 
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
PRINT "       PARSED LINE    Mode: " + strMode + "  X: " + strX + "  Y: " + strY + "  Z: " + strZ + "  AX: " + strAX + "  AY: " + strAY + "  AZ: " + strAZ + "  X1: " + strExtra1 + "  X2: " + strExtra2 + "  x3: " + strExtra3 + "  X4: " + strExtra4

	 
pX = VAL(strX)
pY = VAL(strY)
pZ = VAL(strZ)
pAX = VAL(strAX)
pAY = VAL(strAY)
pAZ = VAL(strAZ)	


DEFPOS point2
DIM xLoop AS INTEGER


SELECT CASE strMode
  CASE "P"
    PRINT "P Mode (moving to point)"
    point2 = (pX,pY,pZ,pAX,pAY,pAZ)
    MOVE P, point2
  CASE "J" 'Move to a set position defining joint angles
	PRINT "J Mode (moving joints to angles)"
	DRIVEA (1,pX),(2,pY),(3,pZ),(4,pAx),(5,pAy),(6,pAZ) 
  CASE "K" 'Move to a set position defining joint angles
	PRINT "K Mode (moving joints to angles relative)"
	DRIVE (1,pX),(2,pY),(3,pZ),(4,pAx),(5,pAy),(6,pAZ) 
  CASE "M"
    PRINT "M Mode (move relative)"
    DRAW L, (pX,pY,pZ)			
  CASE "Q" 'goto point in array
    FOR xLoop = 0 TO arrSize-1 STEP 1
		IF arrName(xLoop) = strX THEN
		   PRINT "moving to point: " + SPRINTF("% d",xLoop) + "  " + arrName(xLoop)
        point2 = (arrX(xLoop),arrY(xLoop),arrZ(xLoop),arrAx(xLoop),arrAy(xLoop),arrAz(xLoop))
        MOVE P, point2			
        xLoop = 900
		END IF
	 NEXT
  CASE "R" 'add point
    FOR xLoop = 0 TO arrSize-1 STEP 1
		IF arrName(xLoop) = "" THEN
		   PRINT "Adding Point: " + SPRINTF("% d",xLoop) + "  " + strExtra1
         working = xLoop
         arrName(working) = strExtra1
         arrX(working) = VAL(strX)
         arrY(working) = VAL(strY)
         arrZ(working) = VAL(strZ)
         arrAx(working) = VAL(strAx)
         arrAy(working) = VAL(strAy)
         arrAz(working) = VAL(strAz)
         xLoop = 900
		END IF
	 NEXT
  CASE "S" 'add cur pos to list strX=Name
	DEFPOS posCur
	posCur = CURPOS
   FOR xLoop = 0 TO arrSize-1 STEP 1
		IF arrName(xLoop) = "" THEN
		   PRINT "Adding Point: " + SPRINTF("% d",xLoop) + "  " + strExtra1
         working = xLoop
         arrName(working) = strX
         arrX(working) = POSX(posCur)
         arrY(working) = POSY(posCur)
         arrZ(working) = POSZ(posCur)
         arrAx(working) = POSRX(posCur)
         arrAy(working) = POSRY(posCur)
         arrAz(working) = POSRZ(posCur)
         xLoop = 900
		END IF
	 NEXT
  CASE "D" 'Dump point array
	FOR xLoop = 0 TO arrSize-1 STEP 1
     IF arrName(xLoop) <> "" Then
       DEFSTR printLine 
		 printLine = "R," + SPRINTF("% d",arrX(xLoop)) + "," + SPRINTF("% d",arrY(xLoop)) + "," + SPRINTF("% d",arrZ(xLoop)) + "," + SPRINTF("% d",arrAx(xLoop)) + ","
       printLine = printLine + SPRINTF("% d",arrAy(xLoop)) + "," + SPRINTF("% d",arrAz(xLoop)) + "," + arrName(xLoop)
       PRINT printLine  
     ENDIF
   NEXT
		
				
		
	

END SELECT	
PRINT "      Current Postion: "
PRINT CURPOS	
PRINT " "
GOTO *BEGIN
END


	

	




