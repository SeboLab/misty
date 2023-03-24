from rospy import Subscriber, Publisher
from std_msgs.msg import Bool, String, Empty, StringArray
from util import post, get, ros_msg_to_json, json_to_ros_msg
from misty_ros.msg import (
    CaptureSpeech,
    VideoRecording,
    RecordVideo,
    TakePicture,
    AssetRequest,
)
from time import sleep

class Perception:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        Subscriber("/audio/speech/capture", CaptureSpeech, self.capture_speech)

        # Takes in a rtmp or rtsp URL
        Subscriber("/avstreaming/start", String, self.start_av_streaming)

        Subscriber("/faces/detection/start", Empty, self.start_face_detection)
        Subscriber("/faces/training/start", String, self.start_face_training)

        Subscriber("/videos/recordings/get", AssetRequest, self.get_video_recording)
        Subscriber("/videos/recordings/list/get", Empty, self.get_video_list)
        self.video_pub = Publisher("/videos/recordings/get/results", VideoRecording)
        self.video_list_pub = Publisher("/videos/recordings/list", StringArray)

        Subscriber("/audio/record/start", String, self.start_recording_audio)
        Subscriber("/video/record/start", RecordVideo, self.start_recording_video)
        Subscriber("/audio/record/stop", Empty, self.stop_recording_audio)
        Subscriber("/video/record/stop", Empty, self.stop_recording_video)
        Subscriber("/cameras/rgb", TakePicture, self.take_picture)

    def start_av_streaming(self, params):
        post(self.ip, "avstreaming/stop")
        sleep(5)
        post(self.ip, "services/avstreaming/enable")
        sleep(8)
        post(self.ip, "avstreaming/start", {"URL": params.data, "Width": 640, "Height": 480, "VideoBitRate": 1000000, "AudioBitRate": 32000})
        

    def start_face_detection(self, params):
        post(self.ip, "faces/detection/start")

    def start_face_training(self, params):
        post(self.ip, "faces/training/start", {"FaceId": params.data})

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

    def get_video_list(self, params):
        self.video_list_pub.publish(get(self.ip, "videos/recordings/list", {}))

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
