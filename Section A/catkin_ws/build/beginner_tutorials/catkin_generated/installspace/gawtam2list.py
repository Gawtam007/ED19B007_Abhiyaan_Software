#!/usr/bin/env python3
# Software License Agreement (BSD License)

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

a = ''

def callback1(data):
    global a
    a += data.data



def callback2(data):
    #rospy.loginfo("Callback2 heard %s",data.data)
    global a 
    a += data.data
    print ("a : ", a)

def gawtam2list():

    global a

    rospy.init_node('gawtam2list', anonymous=True)
    rospy.Subscriber('/team_abhiyaan', String, callback1)
    rospy.Subscriber('/autonomy', String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

if __name__ == '__main__':
    gawtam2list()
    print(a)
