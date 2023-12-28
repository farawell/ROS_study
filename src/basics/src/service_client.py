#!/usr/bin/env python3

import rospy
from basics.srv import WordCount
import sys # To use .join() method

rospy.init_node('service_client')
rospy.wait_for_service('word_count') # Wait for the server to promote the service
# Utilizing the service before it being promoted will cause error,
# which is different form topic.

words = ' '.join(sys.argv[1:]) # command line arguemnts after the function call

# Allow to use 'word_count' as a local function that calls the service
word_counter = rospy.ServiceProxy('word_count', WordCount)
word_count = word_counter(words)

print(words, '->', word_count.count) # final result
