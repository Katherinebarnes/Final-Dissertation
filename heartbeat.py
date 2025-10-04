import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

HR_SENSOR = 12
tempFlag = 0
bpFlag = 0
hrFlag = 0
GPIO.setup(HR_SENSOR,GPIO.IN)

def setHeartRate():
  global tempFlag
  global bpFlag
  global hrFlag
  print ('setHeartRate')
  tempFlag = 0
  bpFlag   = 0
  hrFlag   = 1

def HEART_BEAT():
     if hrFlag == 1 :
      print('Hold The finger On sensor')
      #time.sleep(1) 
      sensorCounter = 0
      startTime     = 0
      endTime       = 0
      rateTime      = 0
      while sensorCounter < 1 and  hrFlag == 1:
        if (GPIO.input(HR_SENSOR)):
          if sensorCounter == 0:
            startTime = int(round(time.time()*1000))
            #print startTime
          sensorCounter = sensorCounter + 1
          #print sensorCounter
          while(GPIO.input(HR_SENSOR)):
            if hrFlag == 0:
              break
            pass

      time.sleep(1)      
      endTime  = int(round(time.time()*1000))
      #print endTime
      rateTime = endTime - startTime
      #print rateTime
      rateTime = rateTime / sensorCounter
      heartRate = (60000 / rateTime) #/ 3 
      heartRate = abs(heartRate)
      heartRate=int(heartRate+20)
      print (heartRate)
      return heartRate
      

