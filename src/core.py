#!/usr/bin/env python

from std_msgs.msg import Float32MultiArray
import requests
import json
from python_to_rest import Robot
from rospy import Subscriber, Publisher
import sys
from misty_ros.msg import Drive

class Core:

    def __init__(self, ip):
        print("hi")
        self.r = Robot(ip)
        self.drive_sub = Subscriber("/Drive", Drive, self.drive)
        self.drive_arc_sub = Subscriber("/Drive/arc", Float32MultiArray, self.drive)
        self.drive_heading_sub = Subscriber("/Drive/heading", Float32MultiArray, self.drive)
        self.drive_time_sub = Subscriber("/Drive/time", Float32MultiArray, self.drive)
        self.drive_track_sub = Subscriber("/Drive/track", Float32MultiArray, self.drive)
        self.halt_sub = Subscriber("/halt", Float32MultiArray, self.drive)
        self.move_arm_sub = Subscriber("/move/arm", Float32MultiArray, self.drive)
        self.move_arms_sub = Subscriber("/move/arms", Float32MultiArray, self.drive)
        self.move_head_sub = Subscriber("/move/head", Float32MultiArray, self.drive)
        self.stop_sub = Subscriber("/stop", Float32MultiArray, self.drive)

    def drive(self, params):
        r.drive(params.linear_velocity, params.angular_velocity)

    def drive_time(self, params):
        r.driveTime(params.linear_velocity, params.angular_velocity, params.time)

    

if __name__ == '__main__':
    Core(sys.argv[1])
