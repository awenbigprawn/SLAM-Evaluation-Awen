#!/bin/bash

source ~/catkin_ws/devel/setup.bash
mkdir ~/vins_result
i=1
for file in ~/Euroc_rosbags/* ;
do
  if [ $i -le 2 ]
  then
    var=$file
    var=${var##*/}
    var=${var%%.*}
    echo $var
    mkdir vins_result
    
    {
    gnome-terminal -t "start_robot" -c "roslaunch vins vins_rviz.launch;exec bash"
    }&
    sleep 0.5s
    {
    gnome-terminal -t "start_vio_node" -c "rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml;exec bash"
    }&
    sleep 0.5s
    {
    gnome-terminal -t "play_rosbag" -c "rosbag play ~/Euroc_rosbags/$var.bag"
    }
    
    python ~/awen_evaluation/csv_to_txt.py
    mv vins_result vins_result_$var
    i=$[i+1]
  fi

  
  mv vins_result ~/vins_result_awen/$var

done
    
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
!



