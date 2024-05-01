#!/usr/bin/env python
from ur_kinematics.ur_kin_py import forward, inverse
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray
from tf import TransformListener

joints_pub = rospy.Publisher('/joint_group_position_controller/command', Float64MultiArray, queue_size=1)
x_scaling = 2
y_scaling = 2
z_scaling = 2


def best_sol(sols, q_guess, weights):
    valid_sols = []
    for sol in sols:
        test_sol = np.ones(6)*9999.
        for i in range(6):
            for add_ang in [-2.*np.pi, 0, 2.*np.pi]:
                test_ang = sol[i] + add_ang
                if (abs(test_ang) <= 2.*np.pi and
                    abs(test_ang - q_guess[i]) < abs(test_sol[i] - q_guess[i])):
                    test_sol[i] = test_ang
        if np.all(test_sol != 9999.):
            valid_sols.append(test_sol)
    if len(valid_sols) == 0:
        return None
    best_sol_ind = np.argmin(np.sum((weights*(valid_sols - np.array(q_guess)))**2,1))
    return valid_sols[best_sol_ind]


def go_to(x, current_q=None):
    if current_q is None:
        current_q = np.array([0.] * 6)
    q_sols = inverse(np.array(x), current_q[5])
    q = best_sol(q_sols, current_q, [1]*6)
    msg = Float64MultiArray()
    msg.data = q
    joints_pub.publish(msg)
    return q


if __name__ == "__main__":
    rospy.init_node('ur_jogging')
    tf = TransformListener()
    rospy.sleep(1)
    t = tf.getLatestCommonTime("/base", "/stylus")

    position, quaternion = tf.lookupTransform("/base", "/stylus", t)

    x = np.array([[1.,  0., -0.,  position[0]*x_scaling],
                  [0., -1.,  0.,  position[1]*y_scaling],
                  [0., -0., -1., position[2]*z_scaling],
                  [0.,  0.,  0.,  1.]])
    current_q = go_to(x)
    rospy.sleep(2)

    r = rospy.Rate(20)
    while not rospy.is_shutdown():
        t = tf.getLatestCommonTime("/base", "/stylus")
        position, quaternion = tf.lookupTransform("/base", "/stylus", t)
        x[0][3] = position[0]*x_scaling
        x[1][3] = position[1]*y_scaling
        x[2][3] = position[2]*z_scaling
        current_q = go_to(x, current_q)
        r.sleep()
