#!/usr/bin/env python3




import rospy
from std_msgs.msg import String 


rospy.init_node('talker') 
pub = rospy.Publisher('chatter', String, queue_size=10) 
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    Fin = String() 
    Fin = input("終了しますか")
    
    pub.publish(Fin) 
    rospy.loginfo("Fin")
    rate.sleep() 