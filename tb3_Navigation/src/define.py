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


P1 = [-3.75, 4.4]
P2 = [-4.23, 0.3]
P3 = [0,0]
P4 = [0.2, 4.0]
P5 = [-3.75, 4.4] 
