# Gazebo
This file contains the entire package for running the example. 

# Setup
**->** Create catkin workspace. (Note: You can follow these steps [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) to make a catkin workspace.) \
**->** In src folder, create catkin package called foot_test by using the command :
 ```
$ catkin_create_pkg foot_test rospy rviz controller_manager gazebo_ros joint_state_publisher joint_state_controller robot_state_publisher
 ```
**->** Copy the contents from the 'Gazebo' directory into 'foot_test'\
**->** Next source your workspace by passing the command:
```
$ source ~/(Your catkin work space name)/devel/setup.bash
```
**->** Pass the command. This will launch the model and the controllers for the joint.
```
$ roslaunch foot_test robot_and_controller.launch
```
**->** Open a **second terminal,** and if you pass the command :
```
$ rostopic list
```
it will show the list of publishable topics for the robot. In this we are gonna use the topic **/foot_test/joint1_position_controller/command** to publish angles to the joint by giving the command:
```
rostopic pub -1 /foot_test/joint1_position_controller/command std_msgs/Float64 "data: 0.0"
```
Where data is the angle (in radians) which you can specify to rotate the joint to. The limits of the joints are **0 to 1.57**.
