I uploaded the catkin's src folder which is ready for the start. For your primary catkin folder's not crash, install this src folder to other catkin directory. make catkin_make. Install dependencies and it is ready to use (still have some problems to solve).
roslaunch camera_turret new_simu.launch
cd /catkin_ws1/src/balloon_simu_2024-2025/22_ball_simu ---> ./new_balloons_simu.sh
 if you want to control the camera of the turret, with joystick:
 
 rosrun camera_turret joy_to_command.py
 
 with keyboard, you should run both of it:
 
 rosrun camera_turret keyboard_to_command.py
 rosrun camera_turret keyboard_reader.py
 
 sudo apt install ros-noetic-gazebo-ros-control
 sudo apt install ros-noetic-gazebo-ros-pkgs
 sudo apt install ros-noetic-joint*
 sudo apt install ros-noetic-joint
 sudo apt install ros-noetic-effort-controllers
 sudo apt install ros-noetic-position-controllers
