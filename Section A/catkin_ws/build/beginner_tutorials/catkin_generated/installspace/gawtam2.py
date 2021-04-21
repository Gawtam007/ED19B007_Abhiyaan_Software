#!/usr/bin/env python3
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String

def gawtam2():

    rospy.init_node('gawtam2', anonymous = True)

    pub1 = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rate = rospy.Rate(0.5)
    rate.sleep()
    str1 = "Team Abhiyaan: "
    pub1.publish(str1)



    str2 = "Fueled By Autonomy" 
    pub2 = rospy.Publisher('/autonomy', String, queue_size=10)
    rate.sleep()
    pub2.publish(str2)


if __name__ == '__main__':
    try:
        gawtam2()
    except rospy.ROSInterruptException:
        pass
