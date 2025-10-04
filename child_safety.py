from heartbeat import *
from onewire_temp import *
import RPi.GPIO as GPIO
import time
import urllib.request
import requests
import threading
import json
import time
import requests
import telepot
bot = telepot.Bot('7267166324:AAH3HvQF4Lz_AGDdRoAw4W4vK531DTvB1r4')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

switch = 26
buzzer=21

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,False)
status = 'Normal'
while True:
    setHeartRate()
    heartbeat_val=HEART_BEAT()
    print("heartbeat",heartbeat_val)
    if(GPIO.input(switch)==False):
        print("emergency....")
        GPIO.output(buzzer,True)
        time.sleep(1)
        GPIO.output(buzzer,False)
        status = 'Emergency'
        bot.sendMessage('6786910686', str('Emergency'))
    else:
        status = 'Normal'
        
    temp_c, temp_f =  read_temp()
    print('Temperature ',temp_c, 'C')

    url = "http://192.168.1.2:5000/update"  # Your backend server URL
    data = {
        "heartbeat": str(heartbeat_val),  # Bin classification as "Recyclable" or "Less Recyclable"
        "temperature": str(int(temp_c)),  # Example fill level, you can update it dynamically based on sensor data
        "lat": '13.172226030756097',
        "lng": '77.53629385304806t',
        'name': 'Sam',
        'last_name': 'Wilson',
        'bg': 'B+',
        'dob': '12/3/2017',
        'gender': 'Male',
        'age': '8',
        'contact': '9876543212',
        'address': 'Ramamurthy Nagar',
        'disability': 'None',
        'status': status
        }
    try:
        response = requests.post(url, json=data)
        print(f"Notification sent. Status code: {response.status_code}")
        print("Response:", response.json())
    except Exception as e:
        print(f"Error sending notification: {e}")
    time.sleep(1)
