import board
import time
import busio
import json
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_requests as requests


esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("MAC addr:", [hex(i) for i in esp.MAC_address])

def connect():
    while not esp.is_connected:
        try:
            esp.connect_AP('SSID', 'PASSWORD')
        except RuntimeError as e:
            print("could not connect to AP, retrying: ",e)
            continue
    requests.set_socket(socket, esp)

# Thingworx
Key = "APPKEY"
urlBase = "ThingWorx URL"
headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":Key}

result=1

def Get(thing, property):
    urlValue = urlBase + 'Things/' + thing + '/Properties/' + property
    try:
        response=requests.get(urlValue, headers=headers)
        value = json.loads(response.text)
        result = int(value["rows"][0][property])
        response.close()
    except Exception as e:
        print(e)
        result=e
    return result



print ("WiFi: ",connect())
while True:
    speed=Get('Thing_Name','Property_Name')
    print(speed)
    time.sleep(1)
