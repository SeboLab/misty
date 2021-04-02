#!/usr/bin/env python
import sys
import argparse

import rospy

import util
from movement import Movement
from expression import Expression


class MistyCore:
    def __init__(self, ip, publish_rate=10):
        self.rate = rospy.Rate(publish_rate)
        self.ip = ip

        if not util.ping_ip(self.ip, timeout=1):
            print("ERROR: Unable to establish a connection to Misty.")
            print("Make sure your device is on the same network as Misty")

            sys.exit(1)

        self.movement_control = Movement(self.ip)
        self.expression_control = Expression(self.ip)

        # self.change_led_sub = Subscriber("/display/led", Color, self.change_led)
        # self.change_image_sub = Subscriber(
        #     "/display/change_image", ImageName, self.change_image
        # )

        # self.play_audio_sub = Subscriber(
        #     "/audio/change_audio", FileName, self.play_audio
        # )
        # self.upload_audio_sub = Subscriber(
        #     "/audio/upload_audio", FileName, self.upload_audio
        # )

        # self.battery_sub = Subscriber(
        #     "/info/battery",
        # )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str)
    args, _ = parser.parse_known_args()

    rospy.init_node("misty_core")

    MistyCore(args.ip)

    rospy.spin()
