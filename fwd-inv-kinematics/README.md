# Robotic Arm Kinematics and Path Planning

In this project mathematical modelling and MATLAB simulations are used to establish the forward and inverse kinematics of the Dobot robotic manipulator. The Dobot consists of five revolute joints and a vacuum end-effector that can be used to lift and move small objects. Kinematics express the relationship between the robot’s link length, joint constraints, and the end-effector within its workspace.  

<p align="center">
  <img src="https://github.com/cmcalder55/fwd_inv_kinematics/blob/main/dobot.jpg?raw=true" alt="Dobot in workspace." width="296" height="290"/>
  <img src="https://github.com/cmcalder55/fwd_inv_kinematics/blob/main/dobot_diagram.png?raw=true" alt="Dobot links and joints." width="296" height="290"/>
</p>

MATLAB functions are used to command the robot as well as simulate its behavior. Mathematical models using the Denavit-Hartenberg (DH) convention were constructed to represent the forward and inverse kinematics of the robot’s motion profile. This model was then translated to MATLAB to predict the end effector position and joint configurations for different inputs. This was also done to determine the robot’s constraints and reachable workspace.  

After the robot successfully moved a ball around using the DH inputs, a series of robot configurations was programmed to lift the ball and move it around an obstacle. A probability road map algorithm was used for collision avoidance.  
