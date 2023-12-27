#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np


def callback(msg):
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    # Find the closest point (the pillar)
    range_min = min([range for range in msg.ranges if range != 0.0])
    range_min_index = msg.ranges.index(range_min)

    print('min:', range_min, 'index: ', range_min_index)

    twist = Twist()
    
    if (range_min < 1.5 and range_min > 0.2):
        if (range_min_index > 350) or (range_min_index < 10):
            twist.linear.x = 0.2
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.4
    else:
        twist.linear.x = 0.0
        twist.angular.z = 0.0

    print('linear.x:', twist.linear.x, 'angular.z:', twist.angular.z)
    pub.publish(twist)


if __name__ == '__main__':
    rospy.init_node('pole_follower', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
