#!/usr/bin/python

import rospy
from std_msgs.msg import String

def call(data):
    print data.data

def subscriber_node():
	rospy.init_node("subscriber_node", anonymous=False)
	rospy.Subscriber("String_topic",String, call)
	rospy.spin()

if __name__ == "__main__":
	subscriber_node()
