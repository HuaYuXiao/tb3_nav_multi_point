#!/usr/bin/env python
from functools import partial
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
import rospy
import time
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def moveStep(client, goal, x, y):
    print('moving')
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0

   # Sends the goal to the action serve
    client.send_goal(goal)
    print('goal set')

   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        # Result of executing the action
        
        print('hello,goal reached')
        # return client.get_result()    


def movebase_client():
    global flag
    print('move:',flag)
   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    pointList = [[-4.23, 0.3],
                 [1.3, -0.7], 
                 [0,0],
                 [0.2, 4.0], 
                 [-3.75, 4.4]]
    
    for point in pointList:
        if flag==False:
            print(point)
            moveStep(client, goal, point[0], point[1])
            flag = True
            print('Reached:',flag)


def laser_callback(msg):
    global flag
    print('cb:',flag)
    if flag == False:
        return
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    # Find the closest point (the pillar)
    range_min = min([range for range in msg.ranges if range != 0.0])
    range_min_index = msg.ranges.index(range_min)

    print('min:', range_min, 'index: ', range_min_index)

    twist = Twist()
    
    if (range_min < 3.0) and (range_min > 0.2):
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

    if (range_min < 0.15) and (range_min > 0.04):
        time.sleep(2)
        flag = False
        print('Reached the wall')



# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
        global flag
        flag = False
        print('start:',flag)
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        movebase_client()  
        rospy.Subscriber('/scan', LaserScan, laser_callback)
        rospy.spin()
              
        # if result:
        #     rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
