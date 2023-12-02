#!/bin/bash
#source ~/catkin_ws/devel/setup.bash

save_path=~/evo_result_vins_history/evo_result_03_vins_estimator
read_path=~/evo_result_vins_history/vins_result_awen_03
mkdir $save_path

for file in $read_path/*;
do
  #if [ $i -le 2 ]
  #then
    var=$file
    var=${var##*/}
    var=${var%%.*}
    echo $var
    
    mkdir $save_path/vins_plot_$var

    #groundtruth = ./Euroc/$var/mav0/vicon0/data.csv
    #groundtruth = ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv

    #evo_ape euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/pose_graph_path.txt --align --save_results $save_path/vins_$var -r trans_part --save_plot $save_path/vins_plot_$var/ATE.pdf #--save_table ./evo_result/vins_plot_$var/trans_table.csv
    #evo_ape euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/pose_graph_path.txt --align --save_results $save_path/vins_${var}_rot -r rot_part -r angle_deg --save_plot $save_path/vins_plot_$var/ARE.pdf #--save_table ./evo_result/vins_plot_$var/rot_table.csv
    #evo_rpe euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/pose_graph_path.txt --align --save_results $save_path/vins_${var}_rpe -r trans_part --delta 0.1 --delta_unit m --save_plot $save_path/vins_plot_$var/RTE.pdf #--save_table ./evo_result/vins_plot_$var/trans_table.csv
    #evo_rpe euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/pose_graph_path.txt --align --save_results $save_path/vins_${var}_rot_rpe -r rot_part -r angle_deg --delta 0.1 --delta_unit m --save_plot $save_path/vins_plot_$var/RPE_rot.pdf #--save_table ./evo_result/vins_plot_$var/rot_table.csv

    evo_ape euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/vins_estimator_path.txt --align --save_results $save_path/vins_$var -r trans_part --save_plot $save_path/vins_plot_$var/ATE.pdf #--save_table ./evo_result/vins_plot_$var/trans_table.csv
    evo_ape euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/vins_estimator_path.txt --align --save_results $save_path/vins_${var}_rot -r rot_part -r angle_deg --save_plot $save_path/vins_plot_$var/ARE.pdf #--save_table ./evo_result/vins_plot_$var/rot_table.csv
    evo_rpe euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/vins_estimator_path.txt --align --save_results $save_path/vins_${var}_rpe -r trans_part --delta 0.1 --delta_unit m --save_plot $save_path/vins_plot_$var/RTE.pdf #--save_table ./evo_result/vins_plot_$var/trans_table.csv
    evo_rpe euroc ./Euroc/$var/mav0/state_groundtruth_estimate0/data.csv $read_path/$var/evo_readable_txt/vins_estimator_path.txt --align --save_results $save_path/vins_${var}_rot_rpe -r rot_part -r angle_deg --delta 0.1 --delta_unit m --save_plot $save_path/vins_plot_$var/RPE_rot.pdf #--save_table ./evo_result/vins_plot_$var/rot_table.csv


    evo_res $save_path/vins_$var --save_table $save_path/vins_plot_$var/trans_table.csv
    evo_res $save_path/vins_${var}_rot --save_table $save_path/vins_plot_$var/rot_table.csv
    evo_res $save_path/vins_${var}_rpe --save_table $save_path/vins_plot_$var/trans_relativ_table.csv
    evo_res $save_path/vins_${var}_rot_rpe --save_table $save_path/vins_plot_$var/rot_relativ_table.csv
    # i=$[i+1]
  #fi
done
sleep 0.1s
python ~/awen_evaluation/analyse_awen_vins.py $save_path $read_path