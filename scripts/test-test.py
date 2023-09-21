#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

rospy.init_node("kame")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(10)
move = Twist()
pose = Pose()

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y
    
while not rospy.is_shutdown() :
    sub = rospy.Subscriber('turtle1/pose', Pose, update_pose)
    move.linear.x = 3
    move.angular.z =0
    if   pose.x > 9.5:
        move.linear.x  = 3
        move.angular.z = 3
        
    elif pose.x <1.5:
        move.linear.x  = 3
        move.angular.z = 3
 
  
    if   pose.y < 1.5:
        move.linear.x  = 3
        move.angular.z = 3
    elif pose.y > 9.5:
        move.linear.x  = 3
        move.angular.z = 3

    rospy.loginfo("x")
    rospy.loginfo(pose.x)
    rospy.loginfo("y")
    rospy.loginfo(pose.y)
    
    pub.publish(move)
    rate.sleep()