#!/usr/bin/env python

# This will subscribe to the tendon_model_publisher's
# /hand_command[s] topic and send commands to the joints
# on the JointEffortController and JointPositionController topics for the joints

# finger1_roll_joint_position
# finger1_prox_joint_effort
# finger1_dist_joint_effort
# finger2_roll_joint_position
# finger2_prox_joint_effort
# finger2_dist_joint_effort
# thumb_prox_joint_effort
# thumb_dist_joint_effort

import rospy
from nasa_hand_control.msg import HandCommand
from nasa_hand_control.msg import HandCommands # array
from std_msgs.msg import Float64

def callback(data):
    # loop through the message and send controller commands
    # if a value is missing, don't set any
    # make sure we have all values

    if len(data.commands) == 8:
        topics = [
        'finger1_roll_joint_position_controller/command',
        'finger1_prox_joint_effort_controller/command',
        'finger1_dist_joint_effort_controller/command',
        'finger2_roll_joint_position_controller/command',
        'finger2_prox_joint_effort_controller/command',
        'finger2_dist_joint_effort_controller/command',
        'thumb_prox_joint_effort_controller/command',
        'thumb_dist_joint_effort_controller/command'
        ]

        for i in range(len(data.commands)):
            pub = rospy.Publisher(topics[i], Float64, queue_size=10) # controller topic
            msg = Float64(data.commands[i]) # single command
            #rospy.loginfo(topics[i] + ' got  ' + str(msg))
            pub.publish(msg)

def send_commands():
    rospy.init_node('hand_commander', anonymous=True) # node that will publish the commands
    rospy.Subscriber('hand_commands', HandCommands, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        send_commands()
    except rospy.ROSInterruptException:
        pass
