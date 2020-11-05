import serial
import numpy as np

orientation_sensor_data = []
new = False
end = False
packet_type = 0
combine = 0

time = 0
xRot = 0
yRot = 0
zRot = 0

packet_select = 3

def return_signed(val, max_bits = 16):
    if val & (1 << (max_bits - 1)):
        val = -1 * (1 << max_bits) + val

    return val

with serial.Serial('COM5', 115200) as ser:
    try:
        while True:
            stream_data = ser.read(50)   # read a '\n' terminated line
            #print(stream_data)
            stream_length = len(stream_data)

            for i in range(stream_length):
                current_data = stream_data[i]
                if stream_data[i] == 0x7E:
                    new = True
                    combine = 0
                    packet_type = 0
                    time = 0
                    xRot = 0
                    yRot = 0
                    zRot = 0
                    if end is False:
                        if orientation_sensor_data == []:
                            continue
                        print(orientation_sensor_data)
                        for i in range(4):
                            time += orientation_sensor_data[3 + i] << (i * 8)

                        time = float(time) / 1e6 
                        print("%.2f" % (time))

                        xRot = orientation_sensor_data[7] + (orientation_sensor_data[8] << 8)
                        yRot = orientation_sensor_data[9] + (orientation_sensor_data[10] << 8)
                        zRot = orientation_sensor_data[11] + (orientation_sensor_data[12] << 8)

                        xRot = float(return_signed(xRot)) * 0.05
                        yRot = float(return_signed(yRot)) * 0.05
                        zRot = float(return_signed(zRot)) * 0.05

                        print("%.2f, %.2f, %.2f" %(xRot, yRot, zRot))

                    end = True
                    orientation_sensor_data = []
                    continue
                if new is True and stream_data[i] == packet_select:
                    new = False
                    end = False
                    combine = 0
                    packet_type = 1
                    orientation_sensor_data.append(0x7E)
                    orientation_sensor_data.append(stream_data[i])
                    continue
                else:
                    new = False

                if packet_type == 1:
                    if stream_data[i] == 0x7D:
                        combine = 0x70
                        continue
                    if combine == 0x70:
                        orientation_sensor_data.append(combine | (stream_data[i] & 0x0F))
                        combine = 0
                        continue
                    else:
                        orientation_sensor_data.append(stream_data[i])

            
    except KeyboardInterrupt:
        print("\nClosing !!!")
        ser.close()



