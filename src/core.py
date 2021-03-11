#!/usr/bin/env python
import argparse

import rospy
from rospy import Subscriber, Publisher
from std_msgs.msg import Float32MultiArray
from misty_ros.msg import Drive, DriveTime, DriveTrack, Color
from python_to_rest import Robot


class MistyCore:
    def __init__(self, ip):
        self.robot = Robot(ip)

        self.change_led_sub = Subscriber("/display/led", Color, self.change_led)
        self.change_image_sub = Subscriber(
            "/display/change_image", ImageName, self.change_image
        )

        self.play_audio_sub = Subscriber(
            "/audio/change_audio", FileName, self.play_audio
        )
        self.upload_audio_sub = Subscriber(
            "/audio/upload_audio", FileName, self.upload_audio
        )

        self.battery_sub = Subscriber(
            "/info/battery",
        )

        self.drive_sub = Subscriber("/drive", Drive, self.drive)
        self.drive_arc_sub = Subscriber("/drive/arc", Float32MultiArray, self.drive)
        self.drive_heading_sub = Subscriber(
            "/drive/heading", Float32MultiArray, self.drive
        )
        self.drive_time_sub = Subscriber(
            "/drive/time", Float32MultiArray, self.drive_time
        )
        self.drive_track_sub = Subscriber(
            "/drive/track", Float32MultiArray, self.drive_track
        )
        self.halt_sub = Subscriber("/halt", Float32MultiArray, self.drive)
        self.move_arm_sub = Subscriber("/move/arm", Float32MultiArray, self.drive)
        self.move_arms_sub = Subscriber("/move/arms", Float32MultiArray, self.drive)
        self.move_head_sub = Subscriber("/move/head", Float32MultiArray, self.drive)
        self.stop_sub = Subscriber("/stop", Float32MultiArray, self.drive)

    def drive(self, params):
        self.robot.drive(params.linear_velocity, params.angular_velocity)

    def drive_time(self, params):
        self.robot.driveTime(params.linear_velocity, params.angular_velocity, params.time)

    def drive_track(self, params):
        self.robot.driveTrack(params.left_track_speed, params.right_track_speed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str)
    args, _ = parser.parse_known_args()

    rospy.init_node("misty_core")

    MistyCore(args.ip)
