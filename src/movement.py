#!/usr/bin/env python
from rospy import Subscriber
from std_msgs.msg import Bool
from misty_ros.msg import Drive, DriveTrack, MoveArm, MoveArms, MoveHead

from util import post, ros_msg_to_json


class Movement:
    def __init__(self, robot_ip):
        self.ip = robot_ip

        Subscriber("/drive", Drive, self.drive)
        Subscriber("/drive/track", DriveTrack, self.drive_track)
        Subscriber("/drive/stop", Bool, self.stop)

        Subscriber("/arms", MoveArm, self.move_arm)
        Subscriber("/arms/set", MoveArms, self.move_arms)

        Subscriber("/head", MoveHead, self.move_head)
        Subscriber("/halt", Bool, self.halt)

    def drive(self, params):
        if not (
            -100 <= params.linear_velocity <= 100
            and -100 <= params.angular_velocity <= 100
        ):
            print("Clamping linear and angular velocities to [-100, 100]")
            params.linear_velocity = min(100, max(-100, params.linear_velocity))
            params.angular_velocity = min(100, max(-100, params.angular_velocity))

        if "time_ms" not in dir(params) or params.time_ms == 0:
            post(self.ip, "drive", ros_msg_to_json(params))
        else:
            self.drive_time(params)

    def drive_time(self, params):
        post(self.ip, "drive/time", ros_msg_to_json(params))

    def drive_track(self, params):
        if not (
            -100 <= params.left_track_speed <= 100
            and -100 <= params.right_track_speed <= 100
        ):
            print("Clamping track velocities to [-100, 100]")
            params.left_track_speed = min(100, max(-100, params.left_track_speed))
            params.right_track_speed = min(100, max(-100, params.right_track_speed))

        post(self.ip, "drive/track", ros_msg_to_json(params))

    def halt(self, params):
        if params.data:
            post(self.ip, "halt", dict())

    def stop(self, params):
        post(self.ip, "drive/stop", {"Hold": params.data})

    def move_arm(self, params):
        post(self.ip, "arms", ros_msg_to_json(params))

    def move_arms(self, params):
        post(self.ip, "arms/set", ros_msg_to_json(params))

    def move_head(self, params):
        data = ros_msg_to_json(params)
        if data["Duration"] == 0:
            data.pop("Duration")

        post(self.ip, "head", data)
