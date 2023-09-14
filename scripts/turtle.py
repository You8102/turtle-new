#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Twist

X=True
Y=True
a=random.uniform(1,5)
b=random.uniform(1,5)
A=0
B=0
x=0
y=0

if __name__ =="__main__":

    rospy.init_node("kame")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()

    while not rospy.is_shutdown():
        
       
        if   x< -40:
            X=True 
        if   y< -40:
            Y=True 
        if   x> 50:
            X=False 
        if  y> 50:
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
 
        x=x+A
        y=y+B
        
        
        pub.publish(move)
        rospy.loginfo(move)
        rate.sleep()
