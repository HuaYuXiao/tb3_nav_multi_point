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
