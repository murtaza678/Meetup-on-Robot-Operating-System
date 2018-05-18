#!/usr/bin/python

import rospy
from std_msgs.msg import String

def publisher_node():
	rospy.init_node("Publisher_node", anonymous=False)
	pub = rospy.Publisher("String_topic",String, queue_size=10)
	while not rospy.is_shutdown():
		string_data = "This is my first node %s" %rospy.get_time()
		pub.publish(string_data)
		rospy.sleep(2)

if __name__ == "__main__":
	publisher_node()
