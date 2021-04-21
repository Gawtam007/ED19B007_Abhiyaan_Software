#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from turtlesim.msg import Pose
#from nav_msgs.msg import Odometry
PI = 3.1415926535897

a = []

def callback(data):
    global a
    a = data
    #print("Turtle 1 pose: ", a.x, a.y )

class TurtleBot:

    def __init__(self, turtlename):
        rospy.init_node('robot_cleaner', anonymous=True)
        print(turtlename+" defined")
        self.velocity_publisher = rospy.Publisher('/'+turtlename+'/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/'+turtlename+'/pose', Pose, self.update_pose)
        
        self.pose = Pose()    
        self.rate = rospy.Rate(10)


    def update_pose(self, data):
         self.pose = data
         self.pose.x = round(self.pose.x, 4)
         self.pose.y = round(self.pose.y, 4) 
         #print(self.pose)

    def lin_move(self, lin_vel, distance):
        
        vel_msg = Twist()
        current_distance = 0
        print("in distance funtion ")
        t0 = rospy.Time.now().to_sec()

        while current_distance <= distance:

            vel_msg.linear.x = lin_vel
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            #print("moving forward ",current_distance)
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            # Setting the current time for distance calculus
            
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            t1=rospy.Time.now().to_sec()
            current_distance = abs(lin_vel)*(t1-t0)
          
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        
    def rotate(self, ang_vel, rel_ang):

        vel_msg = Twist()
        ang_vel = ang_vel*2*PI/360
        rel_ang = rel_ang*2*PI/360
        current_ang = 0
        t0 = rospy.Time.now().to_sec()
        print("In rotate function")

        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = ang_vel

        while current_ang <= rel_ang:

            #print("rotating",current_ang)
            
            # Setting the current time for distance calculus
            
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            t1 = rospy.Time.now().to_sec()
            current_ang = abs(ang_vel)*(t1-t0)
          
        #vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        

def move():

      global a
      #rospy.init_node('robot_cleaner',anonymous=True)
      #print("Turtle 1  defined")
      #rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
      rospy.Subscriber('/turtle1/pose', Pose, callback)
      
      
      #print(pose.x,pose.y)
      '''
      x1 = TurtleBot('turtle1')
      
      print(x1.pose.x, x1.pose.y)
      a = x1.pose.x
      print("##############################    ",a) 
      
      '''

      x = TurtleBot('turtle2')
      print(a)

      x.lin_move(1,a.x-2) #2 units before turtle 1
      print("forward motion complete")
  
      x.rotate(50,60)  
      print("rotate motion complete")

      x.lin_move(1,2)
      print("second forward motion complete")

      x.rotate(-60,60)  
      print("rotate motion complete")

      x.lin_move(1,6)  
      print("rotate motion complete")


if __name__ == '__main__':
    try:
      move()
      print("lin fuc called")
    except rospy.ROSInterruptException:
        pass
