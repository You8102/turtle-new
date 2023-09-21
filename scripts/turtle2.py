#!/usr/bin/env python3

import rospy
import random
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import String
X=True
Y=True
a=random.uniform(2,5)
b=random.uniform(2,5)
A=0
B=0
pose=Pose()
fin=False

def callback(message):
    global fin
    fin=True
    #rospy.loginfo(fin)

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

if __name__ =="__main__":
    sub = rospy.Subscriber('turtle1/pose', Pose, update_pose)
    rospy.init_node("kame")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()

    while (not rospy.is_shutdown()) :

        if fin==True:
            a=0
            b=0
        

        if   pose.x< 1:
            X=True 
        if   pose.y< 1:
            Y=True 
        if   pose.x> 10:
            X=False 
        if  pose.y> 10:
            Y=False 

        if X==False:
            A=a*(-1)
        if X==True:
            A=a
        if Y==False:
            B=b*(-1)
        if Y==True:
            B=b
        
        move.linear.x = A
        move.linear.y = B
 
        
        
        sub = rospy.Subscriber('chatter', String, callback)
        
        

        pub.publish(move)
        #rospy.loginfo(move)
        #rospy.loginfo(fin)
        #rospy.loginfo("x")
        #rospy.loginfo(pose.x)
        #rospy.loginfo("y")
        #rospy.loginfo(pose.y)
        rate.sleep()
