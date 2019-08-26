
import utime, machine, network, ubinascii, ujson, urequests

WiFi = network.WLAN()

mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
print("MAC address: " + mac)


def connect():
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          WiFi.connect("SSID","PASSWORD")
          i=0
          while i < 25 and not WiFi.isconnected():
               utime.sleep_ms(200)
               i=i+1
          if WiFi.isconnected():
               print ("Connection succeeded")
          else:
               print ("Connection failed")     
     return WiFi.isconnected()

# Thingworx
Key = "APPkey". # Use your appkey
urlBase = "Thingworx URL" # Use your ThingWorx URL
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
          data = ujson.loads(value)
          result = data.get("rows")[0].get(property)
     except:
          print('error')
          result = 'error'
     return result
              

print ("WiFi: ",connect())



# Loop
while True:
          Put('Thing_Name', 'Propertry_Name', 'BaseType', Value)
          temp=Get('Thing_Name','Property_Name')
          print(temp)
          utime.sleep(1)


