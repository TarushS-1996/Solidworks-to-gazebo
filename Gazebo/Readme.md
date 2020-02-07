# Gazebo
This file contains the entire package for running the example. 

## Folder and it's content explained
**config** - Contains the joint controller.\
**launch** - Conmtains the launch file for the bot and it's controller.\
**meshes** - Contains the stl files of the robot.\
**scripts** - Contains a simple publisher script called 'main.py'.\
**urdf** - Contains the Universal Robotic Description Format (URDF) file.

# Setup
**>** Create catkin workspace. (Note: You can follow the steps [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) to make a catkin workspace.) \
**>** In src folder, create catkin package called foot_test by using the command :
 ```
$ catkin_create_pkg foot_test rospy rviz controller_manager gazebo_ros joint_state_publisher joint_state_controller robot_state_publisher
 ```
**>** Copy the contents from the 'Gazebo' directory into 'foot_test'\
**>** Next source your workspace by passing the command:
```
$ source ~/(Your catkin work space name)/devel/setup.bash
```
**>** Pass the command to launch the model and the controllers for the joint.
```
$ roslaunch foot_test robot_and_controller.launch
```
**>** Open a **second terminal,** and if you pass the command :
```
$ rostopic list
```
it will show the list of publishable topics for the robot. In this we are gonna use the topic **/foot_test/joint1_position_controller/command** to publish angles to the joint by giving the command:
```
rostopic pub -1 /foot_test/joint1_position_controller/command std_msgs/Float64 "data: 0.0"
```
Where data is the angle (in radians) which you can specify to rotate the joint to. The limits of the joints are **0 to 1.57**.

# Python Script
To control the joint using a python script, I have provided with a simple publisher script in the scripts folder. It will publish the 'position' variable in the script. The default is set to 1.57 radians. To use python to control the joint, first launch the robot following the earlier steps and pass the command:
```
rosrun foot_test main.py
```
This will move the joint to 1.57 radians. You can choose a custom value by just changing the value of the variable 'position' in the python script.



# How to use your own URDF model with this package ?
After using sw2urdf plugin in your solidworks and creating the package for gazebo, you can replace your meshes and urdf files with the files provided in the directory as default and change the name in the launch file to specify your urdf file. You will need to make changes to your urdf file as the sw2urdf plugin doesn't add the gazebo tag and the transmission tag. 

The gazebo tag that needs to be added at the end of your urdf script is as follows
```
  <gazebo>
    <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
      <robotNamespace>/foot_test</robotNamespace>
    </plugin>
  </gazebo>
```
Now for the transmission tag, it can be added before or after the gazebo tag. The basic format is as follows:
```
<transmission name="{Give transmission name}">
    <type>transmission_interface/SimpleTransmission</type>
    <actuator name="{Give your actuator name}">
      <mechanicalReduction>2</mechanicalReduction>
    </actuator>
    <joint name="{Your joint's name to which this transmission is going to be attached}">
      <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
    </joint>
 </transmission>
```
This transmission tag needs to be added for every joint. For clearer idea, I recommend looking at the urdf provided in the package.

We also need to add controllers for the new joints. In this example, the joint type is revolute so I would recommend reading about different controller types to apply for your task. This is just an example for you to start from.  
