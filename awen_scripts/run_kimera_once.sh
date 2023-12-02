#!/bin/bash

#source ~/catkin_ws/devel/setup.bash

mkdir ~/kimera_result
mkdir ~/kimera_result/$1
rm ~/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc/*

waittime=120
if [ "$1" = "MH_01_easy" ]; then
    waittime=190
fi
if [ "$1" = "MH_02_easy" ]; then
    waittime=160
fi
if [ "$1" = "MH_03_medium" ]; then
    waittime=140
fi
if [ "$1" = "V1_01_easy" ]; then
    waittime=150
fi
if [ "$1" = "V1_02_medium" ]; then
    waittime=100
fi
{
gnome-terminal -t "start_robot" -x bash -c "roslaunch kimera_vio_ros kimera_vio_ros_euroc.launch"
}&
sleep 3s

{
gnome-terminal -t "play_rosbag" -x bash -c "rosbag play --clock ~/Euroc_rosbags/$1.bag"
}&sleep ${waittime}s

    
<<!
{
gnome-terminal -t "start_robot" -x bash -c "roslaunch vins vins_rviz.launch;exec bash"
}&

sleep 0.5s
{
gnome-terminal -t "start_vio_node" -x bash -c "rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml;exec bash"
}&

sleep 0.5s
{
gnome-terminal -t "play_rosbag" -x bash -c "rosbag play ~/Euroc_rosbags/MH_01_easy.bag"
}

sleep 190s
python ~/awen_evaluation/csv_to_txt.py
mv ~/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc vins_result_MH_01_easy

python ~/awen_evaluation/csv_to_txt_kimera.py

mv -f ~/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc ~/kimera_result/$1

mkdir ~/catkin_ws/src/Kimera-VIO-ROS/output_logs/Euroc
!



