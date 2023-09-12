#!/usr/bin/env python3
import rospy
import sys
from geometry_msgs.msg import Twist

if __name__ =="__main__":

    rospy.init_node("kame")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    


    while not rospy.is_shutdown():
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1
        pub.publish(vel)
        rospy.loginfo(vel)
        rate.sleep()
