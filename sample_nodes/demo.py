#!/usr/bin/env python
"""Sample program to make Misty move."""

import argparse
import rospy

import rospy
from rospy import Publisher
from misty_ros.msg import Drive


def main():
    print("Setting up publishers")
    drive_pub = Publisher("/drive", Drive, queue_size=1)

    # Need small delay to setup publishers
    sleep(0.5)

    print("Executing commands")
    drive_pub.publish(20, 0, 1000)


if __name__ == "__main__":
    rospy.init_node("misty_demo")

    main()