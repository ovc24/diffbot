#!/usr/bin/env python3
import tf
import rospy

if __name__ == '__main__':

  rospy.init_node('tf_diffbot_full')

  # blink is a contraction of base link
  blink_bfprint = tf.TransformBroadcaster()

  rate = rospy.Rate(50)

  while not rospy.is_shutdown():

    blink_bfprint.sendTransform((0.00, 0.00, 0.003),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base_link","base_footprint")

    rate.sleep()
