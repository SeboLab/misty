from rospy import Subscriber, Publisher
from std_msgs.msg import Bool, String, Empty
from util import post, get, ros_msg_to_json, json_to_ros_msg
from misty_ros.msg import (
    CaptureSpeech,
    VideoRecording,
    RecordVideo,
    TakePicture,
    AssetRequest,
)


class Perception:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        Subscriber("/audio/speech/capture", CaptureSpeech, self.capture_speech)

        Subscriber("/videos/recordings/get", AssetRequest, self.get_video_recording)
        self.video_pub = Publisher("/videos/recordings/get/results", VideoRecording)
        self.video_list_pub = Publisher("/videos/recordings/list")

        Subscriber("/audio/record/start", String, self.start_recording_audio)
        Subscriber("/video/record/start", RecordVideo, self.start_recording_video)
        Subscriber("/audio/record/stop", Empty, self.stop_recording_audio)
        Subscriber("/video/record/stop", Empty, self.stop_recording_video)
        Subscriber("/cameras/rgb", TakePicture, self.take_picture)

    def set_file_name(self, params):
        self.file_name = params.data

    def set_base64(self, params):
        self.base64 = params.data

    def capture_speech(self, params):
        post(self.ip, "audio/speech/capture", ros_msg_to_json(params))

    def get_video_recording(self, params):
        self.video_pub.publish(
            json_to_ros_msg(
                get(
                    self.ip,
                    "videos/recordings",
                    {"Name": params.file_name, "Base64": params.base64},
                )
            )
        )

    def start_recording_audio(self, params):
        post(self.ip, "audio/record/start", {"FileName": params.data})

    def start_recording_video(self, params):
        post(self.ip, "video/record/start", ros_msg_to_json(params))

    def stop_recording_audio(self, params):
        post(self.ip, "audio/record/stop", {})

    def stop_recording_video(self, params):
        post(self.ip, "video/record/stop", {})

    def take_picture(self, params):
        get(self.ip, "cameras/rgb", ros_msg_to_json(params))
