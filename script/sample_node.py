#!/usr/bin/env python

import rospy

def sample_node():

  rospy.init_node('sample_node', anonymous=True)    
  rate = rospy.Rate(50) # 50hz

  while not rospy.is_shutdown():
    rate.sleep()

if __name__ == "__main__":
  try:
    while True:
      sample_node()
  finally:
    rospy.loginfo("exiting")
