#!/usr/bin/env python
from functools import partial
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
import time
import actionlib
from threading import Thread, Event
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import rospy


P1 = [-3.75, 4.2]
P2 = [-4.23, 0.3]
P3 = [0,0]
P4 = [0.2, 4.0]


def move_pillar():
    while True:
        msg = rospy.wait_for_message("/scan", LaserScan, timeout=None)
        print('laser_callback')
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

        # Find the closest point (the pillar)
        range_min = min([range for range in msg.ranges if range != 0.0])
        range_min_index = msg.ranges.index(range_min)

        print('min:', range_min, 'index: ', range_min_index)

        twist = Twist()

        if (range_min < 1.5 and range_min > 0.4):
            if range_min_index > 10 and range_min_index < 180:
                twist.angular.z = (range_min_index - 10)/180.0 * 2.0 + 0.5
            elif range_min_index > 180 and range_min_index < 350:
                twist.angular.z = (range_min_index - 350)/180.0 * 2.0 - 0.5
            elif range_min_index > 350 or range_min_index < 10:
                twist.linear.x = 0.21

        print('linear.x:', twist.linear.x, 'angular.z:', twist.angular.z)
        pub.publish(twist)

        if (range_min < 0.4) and (range_min > 0.04):
            time.sleep(5)
            print('Reached the pillar')
            break



def movebase_client(client, goal, point):
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame
    goal.target_pose.pose.position.x = point[0]
    goal.target_pose.pose.position.y = point[1]
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0

   # Sends the goal to the action serve
    client.send_goal(goal)

   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        # Result of executing the action
        print('Goal reached')


# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('controller')

        # Create an action client called "move_base" with action definition file "MoveBaseAction"
        client = actionlib.SimpleActionClient('move_base' ,MoveBaseAction)
        # Waits until the action server has started up and started listening for goals.
        client.wait_for_server()

        # Creates a new goal with the MoveBaseGoal constructor
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()


        ### 前往P1 ###
        print('Reaching for Point 1')
        movebase_client(client, goal, P1)


        ### 前往P2 ###
        print('Reaching for Point 2')
        movebase_client(client, goal, P2)  


        ### 前往柱1 ###
        print('Reaching for Pillar 1')
        movebase_client(client, goal, [-3.0, 1.0])  
        move_pillar()


        ### 前往P3 ###
        print('Reaching for Point 3')
        movebase_client(client, goal, P3)


        ### 前往柱2 ###
        print('Reaching for Pillar 2')
        movebase_client(client, goal, [-1.0, 0.1])  
        move_pillar()

        ### 前往P4 ###
        print('Reaching for P4')
        movebase_client(client, goal, P4)


        ### 前往柱3 ###
        print('Reaching for Pillar 3')
        movebase_client(client, goal, [-0.3, 3.7])  
        move_pillar()


        ### 前往P1 ###
        print('Reaching for P1')
        movebase_client(client, goal, P1)  


    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
