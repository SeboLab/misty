from misty_ros.msg import Color, DisplayImage,
from util import post, get, ros_msg_to_json
from rospy import Subscriber, Publisher
from std_msgs.msg import Bool, String

class Perception:
    def __init__(self, robot_ip):
        self.ip = robot.ip

        Subscriber("/audio/speech/capture")
        Publisher("/videos/recordings")
        Publisher("/videos/recordings/list")
        Subscriber("/audio/record/start")
        Subscriber("/video/record/start")
        Subscriber("/audio/record/stop")
        Subscriber("/video/record/stop")
        Subscriber("/cameras/rgb")
