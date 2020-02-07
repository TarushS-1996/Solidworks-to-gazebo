#!/usr/bin/env python3
import rospy 
from std_msgs.msg import Float64

def main():
	pub = rospy.Publisher('/foot_test/joint1_position_controller/command', Float64, queue_size=10)
	rospy.init_node('Angle maker', anonymous = True)
	rate = rospy.Rate(50)
	while not rospy.is_shutdown():
		position = 1.57
		rospy.loginfo(position)
		pub.publish(position)
		rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
