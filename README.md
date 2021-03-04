# Misty II Robot

* [Setup out of the box](https://docs.mistyrobotics.com/misty-ii/get-started/meet-misty/)
  * The app sometimes malfunctions and doesn't detect Wifi networks or the robot
* [Tutorial for an online interface to control Misty](https://docs.mistyrobotics.com/misty-ii/get-started/meet-misty/)
  * The camera won't work if the camera service is disabled
    * [Enable camera service](https://docs.mistyrobotics.com/misty-ii/robot/misty-ii/#using-misty-39-s-rgb-camera)
    * However, the `EnableCameraService` command doesn't always work
* [REST API](https://docs.mistyrobotics.com/misty-ii/rest-api/overview/)
  * Usage examples in rest_demo.py
  * [API command documentation](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference)
    * Send POST and GET requests to send commands to Misty. 
  * [Websocket documentation](https://docs.mistyrobotics.com/misty-ii/rest-api/overview/#getting-live-data-from-misty)
    * For the websocket, use the URI `"ws://" + ip + "/pubsub"`
    * I used a Python library called `websockets`