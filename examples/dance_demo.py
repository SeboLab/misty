from src.python_to_rest import Robot
import time

def arm_thing(n):
    for i in range(n):
        r.moveArm("left", -89, 100)
        r.moveArm("right", 89, 100)
        r.moveHead(20, 0, 0, 100)
        time.sleep(.2)
        r.moveArm("left", 89, 100)
        r.moveArm("right", -89, 100)
        r.moveHead(-20, 0, 0, 100)
        time.sleep(.2)

r = Robot("192.168.1.120")
r.driveTime(0, 100, 3000)
arm_thing(5)
time.sleep(3)
r.driveTime(0, -100, 3000)
