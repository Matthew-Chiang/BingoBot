import serial
from time import sleep

past = {}

ser = serial.Serial('/dev/ttyACM0', 9600)

def sendAns(val,coor):
    if val not in past:
        past[val] = coor
        print("val",val)
        print("ans",coor)

        a = str(coor[0])
        b = str(coor[1])

        print("a",a)
        print("b",b)

        ser.write(str.encode(a))
        sleep(.1)
        ser.write(str.encode(b))
