import serial

with serial.Serial('COM5', 115200) as ser:
    try:
        while True:
            line = ser.read(100)   # read a '\n' terminated line
            print(line)
            
    except KeyboardInterrupt:
        print("\nClosing !!!")
        ser.close()



