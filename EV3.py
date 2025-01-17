#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

import urequests
# Create your objects here.
ev3 = EV3Brick()

Key = "api key"
urlBase = "https://pp-21060114127e.portal.ptc.io/Thingworx/"
headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":Key}

def Put(thing, property, type, value):
     urlValue = urlBase + 'Things/' + thing + '/Properties/*'

     propValue = {property:value}
    
     try:
          response = urequests.put(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          print('error with Put')

def Get(thing, property):
     urlValue = urlBase + 'Things/' + thing + '/Properties/' + property
     try:
          response = urequests.get(urlValue,headers=headers)
          value = response.text
          response.close()
          # print(value)
          data = json.loads(value)
          result = data.get("rows")[0].get(property)
     except:
          print('error')
          result = 'error'
     return result
     
def Create(thing, property, type):
     urlValue = urlBase + 'Things/' + thing + '/Services/AddPropertyDefinition'
     propValue = {'name':property,'type':type,"logged":False}
     try:
          response = urequests.post(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          pass
     
     return response

def Delete(thing, property):
     urlValue = urlBase + 'Things/' + thing + '/Services/RemovePropertyDefinition'
     propValue = {'name':property}
     try:
          response = urequests.post(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          pass
     
     return response


Put('Thing Name', 'Property Name', 'STRING', "Value")

# Write your program here.
ev3.speaker.beep()
