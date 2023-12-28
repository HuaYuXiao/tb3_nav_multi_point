from utils import *


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
        find_pillar()


        ### 前往P3 ###
        print('Reaching for Point 3')
        movebase_client(client, goal, P3)


        ### 前往柱2 ###
        print('Reaching for Pillar 2')
        movebase_client(client, goal, [-1.0, 0.1])  
        find_pillar()

        ### 前往P4 ###
        print('Reaching for P4')
        movebase_client(client, goal, P4)


        ### 前往柱3 ###
        print('Reaching for Pillar 3')
        movebase_client(client, goal, [-0.3, 3.7])  
        find_pillar()


        ### 前往P1 ###
        print('Reaching for P1')
        movebase_client(client, goal, P1)  


    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
