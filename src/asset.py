from rospy import Subscriber
from std_msgs.msg import Bool, String
from misty_ros.msg import SaveAudio, SaveImage, SaveVideo, AudioFile

from util import post, get, delete, ros_msg_to_json

class Asset:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        #TODO
        Publisher("/audio/list")
        Publisher("/images/list")
        Publisher("/video/list")

        self.audio_pub = Publisher("/audio/get", AudioFile)
        self.image_pub = Publisher("/images/get", ImageFile)
        self.video_pub = Publisher("/videos/get", VideoFile)

        Subscriber("/set/file_name", String, self.set_file_name)
        Subscriber("/set/base64", Bool, self.set_base64)

        Subscriber("/audio/delete", String, self.delete_audio)
        Subscriber("/images/delete", String, self.delete_image)
        Subscriber("/videos/delete", String, self.delete_video)

        Subscriber("/audio/save", SaveAudio, self.save_audio)
        Subscriber("/images/save", SaveImage, self.save_image)


    def publish_files(self):
        self.audio_pub.publish(json_to_ros_msg(get(ip, "audio", {"FileName": self.file_name, "Base64": self.base64}).json()))
        self.image_pub.publish(json_to_ros_msg(get(ip, "image", {"FileName": self.file_name, "Base64": self.base64}).json()))
        self.video_pub.publish(json_to_ros_msg(get(ip, "video", {"FileName": self.file_name, "Base64": self.base64}).json()))

    def set_file_name(self, params):
        self.file_name = params.data

    def set_base64(self, params):
        self.base64 = params.data

    def delete_audio(self, params):
        delete(ip, "audio", {"FileName": params.data})

    def delete_image(self, params):
        delete(ip, "images", {"FileName": params.data})

    def delete_video(self, params):
        delete(ip, "videos", {"FileName": params.data})

    def save_audio(self, params):

    def save_image(self, params):





