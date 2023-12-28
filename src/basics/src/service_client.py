#!/usr/bin/env python3

import rospy
from basics.srv import WordCount
import sys

rospy.init_node('service_client')
rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)
