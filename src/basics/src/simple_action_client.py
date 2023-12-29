#!/usr/bin/env python3

import rospy
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)

client.wait_for_server() # Redady until the server is ready

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal) # Send the goal to the server

client.wait_for_result() # Wait for the server repsponse

print('Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))