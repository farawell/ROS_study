#!/usr/bin/env python3

import rospy

from basics.srv import WordCount, WordCountResponse

# WordCountResponse() wrapping is unnecessary since only one value is returned
def count_words(request):
    return WordCountResponse(len(request.words.split()))

rospy.init_node('service_server')

service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()