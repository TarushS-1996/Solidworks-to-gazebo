# Gazebo
This file contains the entire package for running the example. 

# Setup
-> Create catkin workspace. (Note: You can follow these steps here to make a catkin workspace.) \
-> In src folder, create catkin package called foot_test by using the command :
 ```
$ catkin_create_pkg foot_test rospy rviz controller_manager gazebo_ros joint_state_publisher joint_state_controller robot_state_publisher
 ```
-> Copy the contents from the 'Gazebo' directory into 'foot_test'\
-> Next source your workspace by passing the command:
```
$ source ~/(Your catkin work space name)/devel/setup.bash
```
-> Pass the command :
```
$ roslaunch foot_test robot_and_controller.launch
```
