#!/usr/bin/env python3

import rospy
from std_msgs.msg import String 


rospy.init_node('talker') 
pub = rospy.Publisher('chatter', String, queue_size=10) 
rate = rospy.Rate(10)
restart=False

#while (not rospy.is_shutdown())
def fin():
    while  (not rospy.is_shutdown()) and restart==False:
        Fin = String() 
        Fin = input("終了しますか")
    
        pub.publish(Fin) 
        #rospy.loginfo("Fin")
        restart=True
        #rate.sleep() 

def re():
    while (not rospy.is_shutdown()) and restart==True:
        Re = String() 
        Re = input("再開しますか")
    
        pub.publish(Re) 
        restart=False
        #rospy.loginfo("Re")
        #rate.sleep() 

while (not rospy.is_shutdown()):
    fin
    
    rate.sleep()

    