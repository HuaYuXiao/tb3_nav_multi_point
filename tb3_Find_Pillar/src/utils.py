from define import *


def find_pillar(pub, twist):
        msg = rospy.wait_for_message("/scan", LaserScan, timeout=None)

        print(msg.ranges)
        print(msg.intensities)





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
