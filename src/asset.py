from rospy import Subscriber, Publisher
from std_msgs.msg import String
from misty_ros.msg import (
    SaveAudio,
    SaveImage,
    AudioFile,
    ImageFile,
    VideoFile,
    AssetRequest,
)

from util import get, delete, json_to_ros_msg, ros_msg_to_json


class Asset:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        # TODO
        Publisher("/audio/list")
        Publisher("/images/list")
        Publisher("/video/list")

        self.audio_pub = Publisher("/audio/get/results", AudioFile)
        self.image_pub = Publisher("/images/get/results", ImageFile)
        self.video_pub = Publisher("/videos/get/results", VideoFile)

        Subscriber("/audio/get", AssetRequest, self.get_audio_file)
        Subscriber("/images/get", AssetRequest, self.get_image)
        Subscriber("/videos/get", AssetRequest, self.get_video)

        Subscriber("/audio/delete", String, self.delete_audio)
        Subscriber("/images/delete", String, self.delete_image)
        Subscriber("/videos/delete", String, self.delete_video)

        Subscriber("/audio/save", SaveAudio, self.save_audio)
        Subscriber("/images/save", SaveImage, self.save_image)

    def get_audio_file(self, params):
        result = get(
            self.ip,
            f"audio?FileName={params.file_name}&Base64={params.base64}",
        ).json()
        self.audio_pub.publish(json_to_ros_msg(result))

    def get_image(self, params):
        result = get(
            self.ip,
            f"images?FileName={params.file_name}&Base64={params.base64}",
        ).json()
        self.image_pub.publish(json_to_ros_msg(result))

    def get_video(self, params):
        result = get(self.ip, "videos", json=ros_msg_to_json(params)).json()
        self.video_pub.publish(json_to_ros_msg(result))

    def delete_audio(self, params):
        delete(self.ip, "audio", {"FileName": params.data})

    def delete_image(self, params):
        delete(self.ip, "images", {"FileName": params.data})

    def delete_video(self, params):
        delete(self.ip, "videos", {"FileName": params.data})

    def save_audio(self, params):
        pass

    def save_image(self, params):
        pass
