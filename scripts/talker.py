#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ =="__main__":

    rospy.init_node("talker_node")
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        talker.publish()
        rate.sleep()