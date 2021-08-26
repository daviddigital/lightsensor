import serial
import time
from datetime import datetime

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()



while True:
    ## add the time
    data1 = str(ser.readline())
    data1 = data1.replace("b","")
    data1 = data1.replace("'","")
    data1 = data1.replace("\\r\\n","")
    if data1 is not None:
        with open("datadump.txt", "a") as myfile:
            myfile.write(str(datetime.now()) + "," + data1 + "\n")
    print(data1)

ser.close()