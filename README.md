# Hospital-Delivery-Robot
Hospital Delivery Robot for Medicine and Samples

# Author
1. `Ho Xiang (A181576)`
2. `Tan Kai Ze (A202383)`

## Instructions
**LAUNCH HOSPITAL WORLD IN GAZEBO**
`roslaunch aws_robomaker_hospital_world hospital.launch`

**RUN SLAM AND RVIZ**
`roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/arckaiv/Desktop/catkin_ws/hospital_rrt_map.yaml`

**INITIATE MULITPOINT NAVIGATION**
`rosrun multipoint_nav multi_point_nav.py`
