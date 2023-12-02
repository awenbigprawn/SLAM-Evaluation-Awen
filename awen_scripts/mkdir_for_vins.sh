#!/bin/bash

#source ~/catkin_ws/devel/setup.bash

mkdir ~/vins_result_awen

for file in ~/Euroc_rosbags/* ;
do
    var=$file
    var=${var##*/}
    var=${var%%.*}
    echo $var
    
    mkdir ~/vins_result_awen/$var



done