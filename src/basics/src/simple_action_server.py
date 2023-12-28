#!usr/bin/env python3

import rospy
import time
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult

# Timer.action
# Area 1: goal, sent from client side
# duration time_to_wait
# ---
# Area 2: result, sent by server when ended
# duration time_elapsed
# uint32 updates_sent
# ---
# Area 3: feedback, sent by server during the action
# duration time_elapsed
# duration time_remaining

def do_timer(goal):
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0
    server.set_succeeded(result) # Telling the server that the goal is accomplished succesfully

rospy.init_node('timer_action_server')

server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
# 'timer': namespace of which the topic will be promoted
# TimerAction: type of the action that the server handles
# do_timer: callback function
# False: preventing the auto-start of the server

server.start()
rospy.spin()
