import requests
import json

# Some example post and get requests
# Set the json parameter in the post request, setting the data parameter doesn't work

ip = "192.168.1.120"
url = "http://" + ip + "/api"

print(
    requests.post(
        url + "/text/display",
        json=json.dumps({"Text": "Hello, world!", "Layer": "MyTextLayer"}),
    ).json()
)

print(requests.post(url + "/led", json='{ "red":0,"green":0,"blue":255 }').json())

print(requests.post(url + "/flashlight", json='{"On": True}').json())

print(requests.get(url + "/images/list").json())

print(requests.post(url + "/services/audio/enable").json())

print(requests.post(url + "/services/camera/enable").json())

print(
    requests.get(
        url + "/cameras/rgb",
        json=json.dumps(
            {
                "Base64": True,
                "FileName": "pic",
                "Width": 600,
                "Height": 800,
                "DisplayOnScreen": True,
                "OverwriteExisting": True,
            }
        ),
    ).json()
)

# Websocket example
uri = "ws://" + ip + "/pubsub"

subscribe_msg = {
    "Operation": "subscribe",
    "Type": "TimeOfFlight",
    "DebounceMs": 100,
    "EventName": "FrontCenterTimeOfFlight",
    "ReturnProperty": None,
    "EventConditions": [{"Property": "SensorId", "Inequality": "=", "Value": "toffc"}],
}
subscribe_msg = json.dumps(subscribe_msg)


import asyncio
import websockets


async def hello():

    async with websockets.connect(uri) as websocket:
        await websocket.send(subscribe_msg)

        while True:

            msg = json.loads(await websocket.recv())

            if msg["eventName"] == "FrontCenterTimeOfFlight":
                callback(msg)


def callback(msg):
    print(msg)


asyncio.get_event_loop().run_until_complete(hello())
