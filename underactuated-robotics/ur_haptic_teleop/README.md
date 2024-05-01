# ur_haptic_teleop

To install this repo, first, we must download the version control software tool vcstool:

    sudo apt install python3-vcstool

Then, download the ur_haptic_teleop.repos file (raw file) to your catkin_ws folder, and run the following commands in the catkin_ws folder:
    
    vcs import --input ur_haptic_teleop.repos
    rosdep install --from-paths src --ignore-src -y
    catkin build

To run the code, call:

    roslaunch ur_haptic_teleop ur_haptic_teleop.launch 

In a separate terminal, navigate to the ur_haptic_teleop package directory and run:

    rosbag play haptic_joystick_test_data.bag 
    
