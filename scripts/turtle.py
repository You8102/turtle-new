#!/usr/bin/env python3
import rospy
import random
from geometry_msgs.msg import Twist
from std_msgs.msg import String
X=True
Y=True
a=random.uniform(2,5)
b=random.uniform(2,5)
A=0
B=0
x=0
y=0
fin=False

def callback(message):
    global fin
    fin=True
    rospy.loginfo(fin)

if __name__ =="__main__":

    rospy.init_node("kame")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()

    while (not rospy.is_shutdown()) :

        if fin==True:
            a=0
            b=0

        if   x< -35:
            X=True 
        if   y< -35:
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
        
        sub = rospy.Subscriber('chatter', String, callback)
        
        

        pub.publish(move)
        #rospy.loginfo(move)
        #rospy.loginfo(fin)
        rate.sleep()
