#!/usr/bin/env python
# from rospy import Subscriber
# from std_msgs.msg import Bool
# from misty_ros.msg import Drive, DriveTrack, MoveArm, MoveArms, MoveHead
#
# from util import post, ros_msg_to_json
#
# import websocket
#
# class Websocket:
#     def __init__(self, robot_ip):
#         self.ip = robot_ip
#
#         Subscriber("/subscribe", String, self.subscribe)
#
#         self.time_of_flight_pub = Publisher("/time_of_flight", TimeOfFlight)
#         self.backpack_pub = Publisher("/backpack", Backpack)
#         self.face_rec_pub = Publisher("/face_rec", FaceRec)
#
#         self.publish()
#
#     def subscribe(self, params):
#         self.subscribe(params.data)
#
#     def publish(self):
#         while(not rospy.is_shutdown()):
#             self.time_of_flight_pub.publish(self.time_of_flight())
#             self.backpack_pub.publish(self.backpack())
#             self.face_rec_pub.publish(self.face_rec())
#
#
#     def backpack(self):
#         if self.backpack_instance is not None:
#             data = self.backpack_instance.data
#             try:
#                 return json.loads(data)["message"]["message"]
#             except:
#                 return json.loads(data)
#
#         else:
#             return " Backpack data is not subscribed, use the command robot_name.subscribe(\"SerialMessage\")"
#
#     def time_of_flight(self):
#         if self.time_of_flight_instance[0] is not None or self.time_of_flight_instance[1] is not None or self.time_of_flight_instance[2] is not None or self.time_of_flight_instance[3] is not None:
#
#             out = "{"
#             for i in range(4):
#                 try:
#                     data_out = json.loads(self.time_of_flight_instance[i].data)
#                     #print(data_out)
#                     out+="\""+data_out["message"]["sensorPosition"]+"\""+":"
#                     out+=str(data_out["message"]["distanceInMeters"])+","
#                 except:
#                     return json.loads(self.time_of_flight_instance[i].data)
#             out = out[:-1]
#             out+="}"
#             return json.loads(out)
#         else:
#             return " TimeOfFlight not subscribed, use the command robot_name.subscribe(\"TimeOfFlight\")"
#
#     def face_rec(self):
#         data = json.loads(self.face_recognition_instance.data)
#         try:
#             out = "{ \"personName\" : \"" + data["message"]["personName"] + "\", \"distance\" : \"" + str(data["message"]["distance"]) + "\", \"elevation\" :\"" + str(data["message"]["elevation"]) + "\"}"
#             return(json.loads(out))
#         except:
#             return json.loads(self.face_recognition_instance.data)
#
#
#     def subscribe(self,Type,value=None,debounce =0):
#         assert isinstance(Type, str), " subscribe: type name need to be string"
#
#         if Type in self.available_subscriptions:
#
#             if Type == "SerialMessage":
#                 if self.backpack_instance is  None:
#                     self.backpack_instance = Socket(self.ip,Type,_value=value, _debounce = debounce)
#                     time.sleep(1)
#
#             elif Type ==  "TimeOfFlight":
#                 if self.time_of_flight_instance[0] is None:
#                     self.time_of_flight_instance[0] = Socket(self.ip,Type,_value="Left", _debounce = debounce)
#                     time.sleep(0.05)
#                     self.time_of_flight_instance[1] = Socket(self.ip,Type,_value="Center", _debounce = debounce)
#                     time.sleep(0.05)
#                     self.time_of_flight_instance[2] = Socket(self.ip,Type,_value="Right", _debounce = debounce)
#                     time.sleep(0.05)
#                     self.time_of_flight_instance[3] = Socket(self.ip,Type,_value="Back", _debounce = debounce)
#                     time.sleep(1)
#
#             elif Type == "FaceRecognition":
#                 if self.face_recognition_instance is None:
#                     self.startFaceRecognition()
#                     print("FaceRecStarted")
#                     self.face_recognition_instance = Socket(self.ip,Type,_value="ComputerVision", _debounce = debounce)
#
#         else:
#             print(" subscribe: Type name - ",Type,"is not recognized by the robot, use <robot_name>.printSubscriptionList() to see the list of possible Type names")
#
#     def unsubscribe(self,Type):
#         assert isinstance(Type, str), " unsubscribe: type name need to be string"
#
#         if Type in self.available_subscriptions:
#
#             if Type == "SerialMessage":
#
#                 if self.backpack_instance is not None:
#                     self.backpack_instance.unsubscribe()
#                     self.backpack_instance = None
#                 else:
#                     print("Unsubscribe:",Type, "is not subscribed")
#
#             elif Type ==  "TimeOfFlight":
#
#                 if self.time_of_flight_instance[0] is not None:
#                     for i in range(4):
#                         self.time_of_flight_instance[i].unsubscribe()
#                         time.sleep(0.05)
#                     self.time_of_flight_instance = [None]*4
#                 else:
#                     print("Unsubscribe:",Type,"is not subscribed")
#
#             if Type == "FaceRecognition":
#
#                 if self.face_recognition_instance is not None:
#                     self.face_recognition_instance.unsubscribe()
#                     self.face_recognition_instance = None
#                     self.stopFaceRecognition()
#                 else:
#                     print("Unsubscribe:",Type, "is not subscribed")
#
#         else:
#             print(" unsubscribe: Type name - ",Type,"is not recognised by the robot, use <robot_name>.printSubscriptionList() to see the list of possible Type names")
#
#
# # Every web socket is considered an instance
# class Socket:
#
#     def __init__(self, ip,Type, _value = None, _debounce = 0):
#
#         self.ip = ip
#         self.Type  = Type
#         self.value = _value
#         self.debounce = _debounce
#         self.data = "{\"status\":\"Not_Subscribed or just waiting for data\"}"
#         self.event_name = None
#         self.ws = None
#         self.initial_flag = True
#
#         dexter = threading.Thread(target=self.initiate)
#         dexter.start()
#
#     def initiate(self):
#         websocket.enableTrace(True)
#         self.ws = websocket.WebSocketApp("ws://"+self.ip+"/pubsub",on_message = self.on_message,on_error = self.on_error,on_close = self.on_close)
#         self.ws.on_open = self.on_open
#         self.ws.run_forever(ping_timeout=10)
#
#     def on_message(self,ws,message):
#         if self.initial_flag:
#             self.initial_flag = False
#         else:
#             self.data = message
#
#     def on_error(self,ws, error):
#         print(error)
#
#     def on_close(self,ws):
#         ws.send(str(self.get_unsubscribe_message(self.Type)))
#         self.data = "{\"status\":\"Not_Subscribed or just waiting for data\"}"
#         print("###",self.Type," socket is closed ###")
#
#     def on_open(self,ws):
#         def run(*args):
#             self.ws.send(str(self.get_subscribe_message(self.Type)))
#         thread.start_new_thread(run, ())
#
#     def unsubscribe(self):
#         self.on_close(self.ws)
#
#     def get_subscribe_message(self,Type):
#
#         self.event_name = str(randint(0,10000000000))
#
#         if Type == "SerialMessage":
#
#             subscribeMsg = {
#                 "Operation": "subscribe",
#                 "Type": "SerialMessage",
#                 "DebounceMs": self.debounce,
#                 "EventName": self.event_name,
#                 "Message": "",
#                 "ReturnProperty": "SerialMessage"}
#
#         elif Type == "TimeOfFlight":
#
#             subscribeMsg = {
#             "$id" : "1",
#             "Operation": "subscribe",
#             "Type": "TimeOfFlight",
#             "DebounceMs": self.debounce,
#             "EventName": self.event_name,
#             "Message": "",
#             "ReturnProperty": "",
#             "EventConditions":
#             [{
#                 "Property": "SensorPosition",
#                 "Inequality": "=",
#                 "Value": self.value
#             }]}
#
#         elif Type == "FaceRecognition":
#
#             subscribeMsg = {
#                 "Operation": "subscribe",
#                 "Type": self.value,
#                 "DebounceMs": self.debounce,
#                 "EventName": self.event_name,
#                 "Message": "",
#                 "ReturnProperty": ""}
#
#         return subscribeMsg
#
#     def get_unsubscribe_message(self,Type):
#
#         if Type == "SerialMessage":
#
#             unsubscribeMsg = {
#                 "Operation": "unsubscribe",
#                 "EventName": self.event_name,
#                 "Message": ""}
#
#         elif Type == "TimeOfFlight":
#
#             unsubscribeMsg = {
#                 "Operation": "unsubscribe",
#                 "EventName": self.event_name,
#                 "Message": ""}
#
#         elif Type == "FaceRecognition":
#
#             unsubscribeMsg = {
#                 "Operation": "unsubscribe",
#                 "EventName": self.event_name,
#                 "Message": ""}
#
#         return unsubscribeMsg
