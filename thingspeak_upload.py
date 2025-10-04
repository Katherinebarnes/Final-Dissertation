from heartbeat import *
from onewire_temp import *
import RPi.GPIO as GPIO
import time
import urllib.request
import requests
import threading
import json
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Setup
GPIO.setmode(GPIO.BCM)

switch = 26
buzzer=21
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer, GPIO.OUT)


API_KEY = ' '
BASE_URL = 'https://api.thingspeak.com/update?api_key=' + API_KEY

# Upload data to ThingSpeak
def thingspeak_post(heartbeat, temperature_c,latitude,longitude):
    try:
        final_url = f"{BASE_URL}&field1={heartbeat}&field2={temperature_c}&field3={latitude}&field4={longitude}"
        response = urllib.request.urlopen(final_url)
        print("Data uploaded to ThingSpeak.")
    except Exception as e:
        print("Error uploading data:", e)

# Main Loop
if __name__ == '__main__':


    while True:
        setHeartRate()

        heartbeat_val = HEART_BEAT()
        print("Heartbeat:", heartbeat_val)

        if GPIO.input(switch) == False:
            print("Emergency....")
            GPIO.output(buzzer, True)
            time.sleep(1)
            GPIO.output(buzzer, False)

        temp_c, temp_f = read_temp()
        print('Temperature:', temp_c, 'C')
        print('Temperature:', temp_f, 'F')
        latitude=5
        longitude=7
        # Upload to ThingSpeak
        thingspeak_post(heartbeat_val, temp_c,latitude,longitude)

        time.sleep(2)  # ThingSpeak allows 15 sec min interval for free accounts
