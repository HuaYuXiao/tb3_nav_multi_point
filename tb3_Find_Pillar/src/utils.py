from define import *


def find_pillar(pub, twist):
    while True:
        msg = rospy.wait_for_message("/scan", LaserScan, timeout=None)

        # Find the closest point (the pillar)
        range_min = min([range for range in msg.ranges if range != 0.0])
        range_min_index = msg.ranges.index(range_min)

        print('min:', range_min, 'index: ', range_min_index)

        if (range_min < 1.5 and range_min > 0.3):
            if (range_min_index > 350) or (range_min_index < 10):
                twist.linear.x = 0.2
                twist.angular.z = 0.0
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.4
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub.publish(twist)
            break

        pub.publish(twist)

        if twist.linear.x == 0.0 and twist.angular.z == 0.0:
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
