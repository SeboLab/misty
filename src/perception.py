from misty_ros.msg import CaptureSpeech, VideoRecording
from util import post, get, ros_msg_to_json, json_to_ros_msg
from rospy import Subscriber, Publisher
from std_msgs.msg import Bool, String, Empty

class Perception:
    def __init__(self, robot_ip):
        self.ip = robot.ip
        self.base64 = True

        Subscriber("/set/file_name", String, self.set_file_name)
        Subscriber("/set/base64", Bool, self.set_base64)

        Subscriber("/audio/speech/capture", CaptureSpeech, self.capture_speech)

        self.video_pub = Publisher("/videos/recordings", VideoRecording)
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
        post(ip, "audio/speech/capture", ros_msg_to_json(params))

    def publish(self):
        self.video_pub.publish(json_to_ros_msg(get(ip, "videos/recordings", {"Name": self.file_name, "Base64": self.base64})))

    def start_recording_audio(self, params):
        post(ip, "audio/record/start", {"FileName": params.data})

    def start_recording_video(self, params):
        post(ip, "video/record/start", ros_msg_to_json(params))

    def stop_recording_audio(self, params):
        post(ip, "audio/record/stop", {})

    def stop_recording_video(self, params):
        post(ip, "video/record/stop", {})

    def take_picture(self, params):
        get(ip, "cameras/rgb", ros_msg_to_json(params))