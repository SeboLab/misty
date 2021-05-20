#!/usr/bin/env python
"""Sample program to make Misty move."""

import argparse
import rospy
from time import sleep

import rospy
from std_msgs.msg import Bool, String, Empty, UInt8
from rospy import Publisher
from misty_ros.msg import Drive, DisplayVideo

def get_audio_list(params):
    printf(params);

def main():
    print("Setting up publishers")
    drive_pub = Publisher("/drive", Drive, queue_size=1)
    blink_pub = Publisher("/blink", Bool, queue_size=1)
    webview_display_pub = Publisher("/webviews/display", String, queue_size=1)
    layer_pub = Publisher("/layer", String, queue_size=1)
    video_display_pub = Publisher("/videos/display", DisplayVideo)
    audio_get_pub = Publisher("/audio/list/get", Empty)

    audio_get_sub = Subscriber("/audio/list", UInt8, get_audio_list)

    # Need small delay to setup publishers
    sleep(0.5)

    print("Executing commands")
    drive_pub.publish(20, 0, 1000)

    layer_pub.publish("Base")
    blink_pub.publish(False);
    webview_display_pub.publish("https://www.google.com/")

if __name__ == "__main__":
    rospy.init_node("misty_demo")

    main()
