import requests
import base64

# Thingworx
Key = "AppkeytoThingworx"
urlBase = "THingworxURL"
headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":Key}

def Put(thing, property, type, value):
     urlValue = urlBase + 'Things/' + thing + '/Properties/*'

     propValue = {property:value}
    
     try:
          response = requests.put(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          print('error with Put')

def Get(thing, property):
     urlValue = urlBase + 'Things/' + thing + '/Properties/' + property
     try:
          response = requests.get(urlValue,headers=headers)
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
          response = requests.post(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          pass
     
     return response

def Delete(thing, property):
     urlValue = urlBase + 'Things/' + thing + '/Services/RemovePropertyDefinition'
     propValue = {'name':property}
     try:
          response = requests.post(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          pass
     
     return response


Put('THINGname', 'PROPERTYname', 'STRING', "value?")

#For Image

image=open("something.jpg","rb")
read_data=image.read()
data=base64.b64encode(read_data)

Put('THINGname','PROPERTYname','STRING',data)




          

