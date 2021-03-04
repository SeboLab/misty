import requests
import json

# Send post requests to make Misty act, and get requests to get information back
# Use json in the post request, setting the data parameter doesn't work

# Some example post and get requests
ip = "192.168.1.120"
url = "http://" + ip + "/api"

print(requests.post(url + "/text/display", json=json.dumps(params = {"Text": "Hello, world!", "Layer": "MyTextLayer"})).json())
    
print(requests.post(url + "/led", json='{ "red":0,"green":0,"blue":255 }').json())

print(requests.post(url + "/flashlight", json='{"On": True}').json())

print(requests.get(url + "/images/list").json())

print(requests.post(url + "/services/audio/enable").json())

with open('speak', 'r') as file:
    data = file.read().replace('\n', '')
    print(requests.post(url + "/tts/speak", json=json.dumps({"text": data})).json())

print(requests.post(url + "/services/camera/enable").json())


# Websocket example
subscribe_msg = {
  "Operation": "subscribe", 
  "Type": "TimeOfFlight",
  "DebounceMs": 100,
  "EventName": "FrontCenterTimeOfFlight",
  "ReturnProperty": None,
  "EventConditions": [{"Property": "SensorId", "Inequality": "=", "Value": "toffc"}]
}
subscribe_msg = json.dumps(subscribe_msg)


import asyncio
import websockets

async def hello():
    uri = "ws://" + ip + "/pubsub"
    async with websockets.connect(uri) as websocket:
        await websocket.send(subscribe_msg)

        while True:
            
            msg = await websocket.recv()
            callback(msg)

async def callback(msgs):
    print(msg)

asyncio.get_event_loop().run_until_complete(hello())