from misty_ros.msg import Color, DisplayImage, DisplayVideo, PlayAudio
from util import post, get, ros_msg_to_json
from rospy import Subscriber
from std_msgs.msg import Bool, String

class Expression:
    def __init__(self, robot_ip):
        self.ip = robot_ip
        self.layer = "DefaultImageLayer"

        Subscriber("/layer", String, self.set_layer)

        Subscriber("/led", Color, self.change_LED)
        Subscriber("/images/display", DisplayImage, self.display_image)
        Subscriber("/text/display", String, self. display_text)
        Subscriber("/videos/display", DisplayVideo, self.display_video)
        Subscriber("/webviews/display", String, self.display_web_view)
        Subscriber("/audio/pause", Bool, self.pause_audio)
        Subscriber("/audio/play", PlayAudio, self.play_audio)
        Subscriber("/flashlight", Bool, self.set_flashlight)
        Subscriber("/tts/speak", String, self.speak)

    def set_layer(self, params):
        self.layer = params.data

    def change_LED(self, params):
        if params.red in range(0, 256) and params.blue in range(0, 256) and params.green in range(0, 256):
            post(self.ip, "led", {"red": params.red, "green": params.green, "blue": params.blue})

    def display_image(self, params):
        json = ros_msg_to_json(params)
        json["Layer"] = self.layer
        post(self.ip, "images/display", json)

    def display_text(self, params):
        post(self.ip, "text/display", {"Text": params.data, "Layer": self.layer})

    def display_video(self, params):
        json = ros_msg_to_json(params)
        json["Layer"] = self.layer
        post(self.ip, "videos/display", json)

    def display_web_view(self, params):
        post(self.ip, "webviews/display", {"URL": params.data, "Layer": self.layer})

    def pause_audio(self, params):
        post(self.ip, "audio/pause")

    def play_audio(self, params):
        post(self.ip, "audio/play", ros_msg_to_json(params))

    def set_flashlight(self, params):
        post(self.ip, "flashlight", {"On": params.data})

    def speak(self, params):
        post(self.ip, "tts/speak", {"Text": params.data})
