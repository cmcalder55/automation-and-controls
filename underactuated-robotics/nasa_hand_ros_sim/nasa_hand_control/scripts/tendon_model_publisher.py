#!/usr/bin/env python

# HandCommands
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
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

def callback(data):
    # use joint_states to compute commands; then publish
    pub = rospy.Publisher('hand_commands', HandCommands, queue_size=10)

    # Long: Your code starts here.
    commands = [1,0,0,1,0,0,0,0]
    # Long: Your code ends here.

    msg = HandCommands(commands)
    # rospy.loginfo(msg)
    pub.publish(msg)

def get_torques():
    rospy.init_node('tendon_model', anonymous=True) # tendon model node
    rospy.Subscriber('/joint_states', JointState, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        get_torques()
    except rospy.ROSInterruptException:
        pass
