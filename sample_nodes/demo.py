import argparse
import rospy

from misty_ros.core import MistyCore

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, required=True)
    args, _ = parser.parse_known_args()

    rospy.init_node("misty_core")

    MistyCore(args.ip)

    rospy.spin()
