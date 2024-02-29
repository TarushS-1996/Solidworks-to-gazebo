# Solidworks-to-gazebo
A simple example for designing a servo motor in solidworks and simulating it in gazebo.
The package contains :\
 -> Gazebo package.\
 -> Solidworks assembly model.

# Demo Video:
[link](https://photos.google.com/share/AF1QipPB3P8p8guE3lHyMTy4HkaM1XwUcWW5E-WmM2qCJisWc9ShOFBMWjnbi0cqvdgLLQ?key=TnREM1lrUTBZSk5VdkVibU5UMmFWbkVpUmJWc2Fn)
 
 # Solidworks
 The file consists of the assembly of the servo motors, clamp and the end effector. This requires the; 'sw2urdf' plugin to convert the solidworks to a gazebo based package. I will also be going over the conversion of the solidworks file into Gazebo package.
 
  # Gazebo 
 The file consists of necessary launch files, controller files and python example script in the directories launch, config and scripts respectively. I will also be providing descriptions of the directories for better explanation. 
 
 The prerequisits for this package is having:\
 ->Catkin\
 -> ROS-Melodic (all packages installed)
 ### Disclaimer:
 The PID values are not perfectly tuned so when selecting values values between 0 to 1.57 which corresponds to angle of rotation in radians for the joint, the model stutters. However if 0 or 1.57 i.e the maximum values are selected for the endeffector to actuate to, there is no stutter thus showing that PID values are not tuned.
 
