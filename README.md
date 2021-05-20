# Misty II Robot

## Setup

1. Turn Misty on by turning the switch located on the bottom
2. Connect Misty to the same Wifi as your computer using these [instructions](https://docs.mistyrobotics.com/tools-&-apps/mobile/misty-app/). Note the IP of Misty.
   * Note: The phone app for Misty sometimes malfunctions and doesn't detect Wifi networks or the robot. Restart the app and try again if this occurs.

## Usage

1. Clone this repository into `~/catkin_ws/src`
2. cd into the Catkin workspace: `cd ~/catkin_ws`
2. Build the package with `catkin_make`
3. `source devel/setup.bash`
4. Launch the core backend:

```
roslaunch misty_ros misty_ros.launch ip:=<robot ip>
```

5. Publish to ROS topics to control Misty. This can be done in a new command line window or using Python.

   * Example in the command line: `rostopic pub /led misty_ros/Color 255 0 255`
   * Note: run `source devel/setup.bash` in the command line first
   * To see a list of all the topics, run `rostopic list`
   * To see the type of a topic, run `rostopic type </topic/path>`

### Demo

* ```roslaunch misty_ros misty_ros_demo.launch```

   * Note: May need to enable executable permission of Python file with `chmod +x demo.py`


## ROS Topics

* ROS topic paths are mostly the same as the endpoints in the REST API. See the [REST API Documentation](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/) for functionality.
* There are some exceptions:
   * `/layer` sets the layer on the screen to display things in the Expression class
   * Getting data from the robot involves publishing a request in one topic and receiving the data in a separate topic
* The files `src/asset.py`, `src/expression.py`, `src/movement.py`, and `src/perception.py` contain classes which initialize ROS topics
* The core launch file is located in `launch/misty_ros.launch`. Launching this runs `src/core.py` which calls the classes in the other Python files
* ROS messages are stored in `msg`. Make sure to include them in CMakeLists.txt

## Robot Info

* There is an [online interface to control Misty](https://docs.mistyrobotics.com/misty-ii/get-started/meet-misty/) that is useful for testing functionality
* There may be a bug where the camera or audio do not work and the API call to [enable camera service](https://docs.mistyrobotics.com/misty-ii/robot/misty-ii/#using-misty-39-s-rgb-camera) does not fix it. This will require the robot to be returned to the manufacturer.
* Misty has a [REST API](https://docs.mistyrobotics.com/misty-ii/rest-api/overview/). To use the REST API, send POST and GET requests to Misty to control her.
   * Usage examples in `examples/rest_demo.py`
   * [REST API command documentation](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference)
* Misty also has a Websocket server that allows you to receive continuous data
   * [Websocket documentation](https://docs.mistyrobotics.com/misty-ii/rest-api/overview/#getting-live-data-from-misty)
* We took inspiration from [this wrapper](https://github.com/MistyCommunity/Wrapper-Python) that converts Python functions to REST calls

## Progress

* Everything in `src/expression.py` and `src/movement.py` have been tested except for topics involving audio and camera
* `src/perception.py`, and `src/asset.py` have not been tested
* Plan on figuring out how to store string arrays to get lists of file names in `src/asset.py`
* `src/websocket.py` is a work in progress
