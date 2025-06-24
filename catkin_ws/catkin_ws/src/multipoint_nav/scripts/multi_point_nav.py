#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion

def create_goal(x, y, z, qx, qy, qz, qw):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation = Quaternion(qx, qy, qz, qw)
    return goal

if __name__ == '__main__':
    rospy.init_node('multi_point_navigation')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()
    rospy.loginfo("Connected to move_base action server.")

    # Named waypoints
    waypoint_names = [
        "Spawn",
        "Room 1",
        "Room 2",
        "Room 3",
        "Room 4"
    ]

    waypoints = [
        create_goal(-0.334, 2.000, 0.009, -0.001, 0.001, 0.753, 0.658),   # Spawn
        create_goal(-7.918, -6.110, 0.009, -0.001, 0.001, 0.694, 0.720),  # Room 1
        create_goal(6.872, -6.575, 0.009, -0.001, 0.001, 0.740, 0.673),   # Room 2
        create_goal(-2.800, -0.050, 0.009, 0.001, 0.001, -0.706, 0.708),  # Room 3
        create_goal(2.594, -1.000, 0.010, -0.000, 0.000, -0.663, 0.749)    # Room 4
    ]

    while not rospy.is_shutdown():
        print("\nAvailable waypoints:")
        for i, name in enumerate(waypoint_names):
            print(f"{i + 1}: {name}")
        print("x: Exit")

        user_input = input("\nEnter waypoint number(s) to visit (e.g. 1 3) or 'x' to exit: ").strip()

        if user_input.lower() == 'x':
            rospy.loginfo("Exiting multi-point navigation.")
            break

        try:
            selected_indices = [int(x) - 1 for x in user_input.split()]
        except ValueError:
            rospy.logerr("Invalid input. Please enter numbers separated by spaces or 'x' to exit.")
            continue

        for i in selected_indices:
            if 0 <= i < len(waypoints):
                rospy.loginfo(f"Navigating to {waypoint_names[i]} (Waypoint {i + 1})...")
                client.send_goal(waypoints[i])
                client.wait_for_result()
                rospy.loginfo(f"Reached {waypoint_names[i]}.")
            else:
                rospy.logwarn(f"Waypoint index {i + 1} is out of range.")

