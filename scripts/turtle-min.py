#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("kame")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(10)
move = Twist()

while not rospy.is_shutdown() :
    move.linear.x = 1
    move.angular.z =1
    pub.publish(move)
    rate.sleep()



