from define import *


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
        # return client.get_result()    




def find_pole():
    pass




# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')


        # Create an action client called "move_base" with action definition file "MoveBaseAction"
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        # Waits until the action server has started up and started listening for goals.
        client.wait_for_server()

        # Creates a new goal with the MoveBaseGoal constructor
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()


        ### 前往P1 ###
        print('Reaching for P1')
        movebase_client(client, goal, P1)  


        ### 前往P2 ###
        print('Reaching for P2')
        movebase_client(client, goal, P2)  


        ### 前往柱1 ###



        ### 前往P3 ###
        print('Reaching for P3')
        movebase_client(client, goal, P3)


        ### 前往柱2 ###


        ### 前往P4 ###
        print('Reaching for P4')
        movebase_client(client, goal, P4)


        ### 前往柱3 ###


        ### 前往P1 ###
        print('Reaching for P1')
        movebase_client(client, goal, P1)  



        #rospy.Subscriber('/scan', LaserScan, laser_callback)
        #ospy.spin()
              
        # if result:
        #     rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
