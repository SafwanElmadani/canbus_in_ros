#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import PointStamped
#include "visualization_msgs/Marker.h"
from visualization_msgs.msg import Marker
import datetime as dt
import csv

# file=open("lead_speed_est.csv", 'w')
# writer=csv.writer(file)
# writer.writerow(["time","speed"])

def _callback(data):
    print("*************************************************")
    print(data.data)





def listener():
    rospy.init_node('listener', anonymous=True)
    print(rospy.Time.now().to_sec())
    rospy.Subscriber("/realtime_raw_data", String, _callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
