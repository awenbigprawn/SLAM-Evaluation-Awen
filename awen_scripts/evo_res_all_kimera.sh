mkdir ~/evo_result

wenjianjia='kimera_result'
for file in ~/$wenjianjia/* ;
do
  #if [ $i -le 2 ]
  #then
    
    var=$file
    var=${var##*/}
    var=${var%%.*}
    echo $var
    
    mkdir ~/evo_result/kimera_plot_$var
    cd ~/$wenjianjia/$var/Euroc_03
    #python ~/awen_evaluation/csv_to_txt_kimera.py


    evo_ape euroc ~/Euroc/$var/mav0/state_groundtruth_estimate0/data.csv ./traj_pgo.txt --align --save_results ~/evo_result/kimera_$var -r trans_part --save_plot ~/evo_result/kimera_plot_$var/ATE.pdf
    
    evo_ape euroc ~/Euroc/$var/mav0/state_groundtruth_estimate0/data.csv ./traj_pgo.txt --align --save_results ~/evo_result/kimera_${var}_rot -r rot_part -r angle_deg --save_plot ~/evo_result/kimera_plot_$var/ARE.pdf
    
    evo_rpe euroc ~/Euroc/$var/mav0/state_groundtruth_estimate0/data.csv ./traj_pgo.txt --align --save_results ~/evo_result/kimera_${var}_rpe -r trans_part --delta 0.1 --delta_unit m --save_plot ~/evo_result/kimera_plot_$var/RTE.pdf
    
    evo_rpe euroc ~/Euroc/$var/mav0/state_groundtruth_estimate0/data.csv ./traj_pgo.txt --align --save_results ~/evo_result/kimera_${var}_rot_rpe -r rot_part -r angle_deg --delta 0.1 --delta_unit m --save_plot ~/evo_result/kimera_plot_$var/RPE_rot.pdf
    
    evo_res ~/evo_result/kimera_$var --save_table ~/evo_result/kimera_plot_$var/trans_table.csv
    
    evo_res ~/evo_result/kimera_${var}_rot --save_table ~/evo_result/kimera_plot_$var/rot_table.csv
    
    evo_res ~/evo_result/kimera_${var}_rpe --save_table ~/evo_result/kimera_plot_$var/trans_relativ_table.csv
    
    evo_res ~/evo_result/kimera_${var}_rot_rpe --save_table ~/evo_result/kimera_plot_$var/rot_relativ_table.csv
    
    cd ~
    # i=$[i+1]
  #fi
done
sleep 0.5s
python ~/awen_evaluation/analyse_awen_kimera.py