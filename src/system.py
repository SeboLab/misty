#!/usr/bin/env python
from rospy import Subscriber
from std_msgs.msg import Bool, StringArray
from misty_ros.msg import Drive, DriveTrack, MoveArm, MoveArms, MoveHead

from util import post, delete, ros_msg_to_json

class System:
    def __init__(self, robot_ip):
        self.ip = robot_ip
        Subscriber("/text/clear", Empty, self.clear_text)
        Subscriber("/networks/connect", String, self.connect_to_wifi)

        Subscriber("/services/audio/disable", Empty, self.disable_audio_service)
        Subscriber("/services/camera/disable", Empty, self.disable_camera_service)
        Subscriber("/services/slam/disable", Empty, self.disable_slam_service)

        Subscriber("/services/audio/enable", Empty, self.enable_audio_service)
        Subscriber("/services/camera/enable", Empty, self.enable_camera_service)
        Subscriber("/services/slam/enable", Empty, self.enable_slam_service)

        Subscriber("/networks/delete", String, self.forget_wifi)
        Subscriber("/networks/scan", Empty, self.get_available_wifi_networks)

        Subscriber("/services/audio/get_enabled", Empty, self.audio_service_enabled)
        Subscriber("/services/camera/get_enabled", Empty, self.camera_service_enabled)

        Subscriber("/battery/get", Empty, self.get_battery)

        network_pub = Publisher("/networks/result", StringArray)
        audio_service_pub = Publisher("/services/audio/enabled", Boolean)
        camera_service_pub = Publisher("/services/camera/enabled", Boolean)
        battery_pub = Publisher("/battery/level", Battery)

    def clear_text(self, params):
        post(self.ip, "text/clear", {})

    def connect_to_wifi(self, params):
        post(self.ip, "networks", {"NetworkID": params.data})

    def disable_audio_service(self, params):
        post(self.ip, "services/audio/disable", {})

    def disable_camera_service(self, params):
        post(self.ip, "services/camera/disable", {})

    def disable_slam_service(self, params):
        post(self.ip, "services/slam/disable", {})


    def enable_audio_service(self, params):
        post(self.ip, "services/audio/enable", {})

    def enable_camera_service(self, params):
        post(self.ip, "services/camera/enable", {})

    def enable_slam_service(self, params):
        post(self.ip, "services/slam/enable", {})

    def forget_wifi(self, params):
        delete(self.ip, "networks", {"NetworkId": params.data})

    def get_available_wifi_networks(self, params):
        network_pub.publish(get(self.ip, "networks/scan" {}))

    def audio_service_enabled(self, params):
        audio_service_pub.publish(get(self.ip, "services/audio/enabled", {}))

    def camera_service_enabled(self, params):
        camera_service_pub.publish(get(self.ip, "services/camera/enabled", {}))

    def get_battery(self, params):
