import network, usocket, ujson
​
# AP info
SSID='FCHD-CHET' # Network SSID
KEY='CHET1234!@#$'  # Network key
​
# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")
​
wlan = network.WINC()
wlan.connect(SSID, KEY)
​
# We should have a valid IP now via DHCP
print(wlan.ifconfig())
​
def http_get(url):
      _, _, host, path = url.split('/', 3)
      print(host)
      addr=usocket.getaddrinfo(host,80)[0][-1]
      print(addr)
      s=usocket.socket()
      s.connect(addr)
      s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
      data=s.recv(1024)

url='http://api.openweathermap.org/data/2.5/weather?zip=02155,us&appid=c596465aaa95bbc2541646d5f484d5c5'
http_get(url)
