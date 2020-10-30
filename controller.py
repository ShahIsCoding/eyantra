#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

def odom_callback(data):
    global x_position
    x_position=data.pose.pose.position.x

def main():
    rospy.init_node('ebot_controller',anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rate = rospy.Rate(10) 

    velocity_msg = Twist()
    while not rospy.is_shutdown():
        velocity_msg.angular.z=0.2
        velocity_msg.linear.x=5-x_position
    	pub.publish(velocity_msg)
    	print("Controller message pushed at {}".format(rospy.get_time()))
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

