cmake_minimum_required(VERSION 3.0.2)
project(misty_ros)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs
    message_generation
)


## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Drive.msg
   DriveTrack.msg
   MoveArm.msg
   MoveArms.msg
   MoveHead.msg

   Color.msg
   DisplayImage.msg
   DisplayVideo.msg
   PlayAudio.msg
   AssetRequest.msg
   SaveAudio.msg
   SaveImage.msg
   AudioFile.msg
   ImageFile.msg
   VideoFile.msg
   CaptureSpeech.msg
 )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
 )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################


###################################
## catkin specific configuration ##
###################################

catkin_package(
   CATKIN_DEPENDS message_runtime
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
 ${catkin_INCLUDE_DIRS}
)
