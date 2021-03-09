from std_msgs.msg import Float32MultiArray
import requests
import json

class Movement:

    def __init__(self):
        
        self.drive_sub = Subscriber("/drive", Float32MultiArray, self.drive)
        self.drive_arc_sub = Subscriber("/drive/arc", Float32MultiArray, self.drive)
        self.drive_heading_sub = Subscriber("/drive/heading", Float32MultiArray, self.drive)
        self.drive_time_sub = Subscriber("/drive/time", Float32MultiArray, self.drive)
        self.drive_track_sub = Subscriber("/drive/track", Float32MultiArray, self.drive)
        self.halt_sub = Subscriber("/halt", Float32MultiArray, self.drive)
        self.move_arm_sub = Subscriber("/move/arm", Float32MultiArray, self.drive)
        self.move_arms_sub = Subscriber("/move/arms", Float32MultiArray, self.drive)
        self.move_head_sub = Subscriber("/move/head", Float32MultiArray, self.drive)
        self.stop_sub = Subscriber("/stop", Float32MultiArray, self.drive)


    def drive(self, arr):
        requests.post(url + "/drive", )
