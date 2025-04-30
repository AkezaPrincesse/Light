import subprocess
import json
import serial
import time
from datetime import datetime

# Configure serial connection to Arduino
SERIAL_PORT = '/dev/ttyACM0'  # Adjust based on your system
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for serial connection to initialize

def handle_schedule(payload):
    try:
        schedule = json.loads(payload)
        on_time = schedule['on']
        off_time = schedule['off']
        
        while True:
            current_time = datetime.now().strftime('%H:%M')
            
            if current_time == on_time:
                ser.write(b'1')  # Send ON command
                print(f"Light ON at {current_time}")
            elif current_time == off_time:
                ser.write(b'0')  # Send OFF command
                print(f"Light OFF at {current_time}")
                
            time.sleep(60)  # Check every minute
            
    except Exception as e:
        print(f"Error processing schedule: {e}")

def mqtt_subscribe():
    process = subprocess.Popen(
        ['mosquitto_sub', '-t', 'light/schedule'],
        stdout=subprocess.PIPE,
        text=True
    )
    
    for line in process.stdout:
        if line.strip():
            handle_schedule(line.strip())

if __name__ == "__main__":
    try:
        mqtt_subscribe()
    except KeyboardInterrupt:
        print("Shutting down...")
        ser.close()