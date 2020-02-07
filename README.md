# Solidworks-to-gazebo
A simple example for designing a servo motor in solidworks and simulating it in gazebo.
The package contains :\
 -> Gazebo package.\
 -> Solidworks assembly model.
 
 # Gazebo 
 The file consists of necessary launch files, controller files and python example script in the directories launch, config and scripts respectively. I will also be providing descriptions of the directories for better explanation. 
 ## Disclaimer:
 The PID controls are not perfectly tuned so when selecting values values between 0 to 1.57 which corresponds to angle of rotation in radians for the joint, the model stutters. However if 0 or 1.57 i.e the maximum values are selected for the endeffector to actuate to, there is no stutter thus showing that PID values are not tuned.
 
 # Solidworks
 The file consists of the assembly of the servo motors, clamp and the end effector. 
