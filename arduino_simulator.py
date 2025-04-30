
import serial

ser = serial.Serial('COM6', 9600)  

print("Simulated Arduino ready.")
while True:
    if ser.in_waiting:
        command = ser.read().decode().strip()
        if command == '1':
            print("Light ON")
        elif command == '0':
            print("Light OFF")
