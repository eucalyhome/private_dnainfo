import serial
import time
import os

con = serial.Serial('/dev/ttyACM0', 115200, timeout=100)

def getdata(querydata):
    while True:
        try:
            outputstring = querydata + "\n"
            serialline = ""
            con.write(bytes(outputstring))
            while True:
                for serialreaddata in con.read():
                    serialline += serialreaddata
                    if serialreaddata == '\n':
                        serialline = serialline.strip()
                        return (serialline)
        except:
            time.sleep(0.1)
            return("notfound")

def main():
    while True:
        dnab = getdata("B=GET")
        dnai = getdata("I=GET RAW")
        dnav = getdata("V=GET RAW")
        dnar  = getdata("R=GET RAW")
        dnap = getdata("E=GET PRODUCT")
        dnae = getdata("S=GET MEAN ENERGY")
        dnaw = getdata("S=GET MEAN POWER")
        print (" BAT:" + dnab +
               " CUR:" + dnai +
               " VOL:" + dnav +
               " REG:" + dnar +
               " PRO:" + dnap +
               " ENE:" + dnae +
               " WAT:" + dnaw )

if __name__ == '__main__':
    main()