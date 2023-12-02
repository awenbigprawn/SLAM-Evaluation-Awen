#!/bin/bash

#source ~/catkin_ws/devel/setup.bash

mkdir ~/vins_result
mkdir ~/vins_result/evo_readable_txt

{
gnome-terminal -t "start_robot" -x bash -c "roslaunch vins vins_rviz.launch"
}&
sleep 0.7s

{
gnome-terminal -t "start_vio_node" -x bash -c "rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml"
}&
sleep 0.7s

{
gnome-terminal -t "start_lcd_node" -x bash -c "rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml"
}&
sleep 0.7s

{
gnome-terminal -t "awen_record_node" -x bash -c "rosrun vins awen_evaluate"
}&
sleep 0.7s

{
gnome-terminal -t "play_rosbag" -x bash -c "rosbag play ~/Euroc_rosbags/$1.bag"
}





    
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
mv vins_result vins_result_MH_01_easy

python ~/awen_evaluation/csv_to_txt.py
mv -f vins_result ~/vins_result_awen/$1
!



