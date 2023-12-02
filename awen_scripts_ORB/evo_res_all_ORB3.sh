
mkdir -p ~/result_orb_evo/result03
save_path=~/result_orb_evo/result03
read_path=~/result_orb/euroc_result_03
for file in $wenjianjia/*;
do
    var=$file
    var=${var##*/}
    echo $var

    mkdir -p $save_path/orb_plot_$var

    evo_ape euroc ~/Euroc_GT/$var/data.csv $read_path/$var/traj_evo.txt --align --save_results $save_path/orb_$var -r trans_part --save_plot $save_path/orb_plot_$var/ATE.pdf
    evo_ape euroc ~/Euroc_GT/$var/data.csv $read_path/$var/traj_evo.txt --align --save_results $save_path/orb_${var}_rot -r rot_part -r angle_deg --save_plot $save_path/orb_plot_$var/ARE.pdf
    evo_rpe euroc ~/Euroc_GT/$var/data.csv $read_path/$var/traj_evo.txt --align --save_results $save_path/orb_${var}_rpe -r trans_part --delta 0.1 --delta_unit m --save_plot $save_path/orb_plot_$var/RTE.pdf
    evo_rpe euroc ~/Euroc_GT/$var/data.csv $read_path/$var/traj_evo.txt --align --save_results $save_path/orb_${var}_rot_rpe -r rot_part -r angle_deg --delta 0.1 --delta_unit m --save_plot $save_path/orb_plot_$var/RPE_rot.pdf
    
    evo_res $save_path/orb_$var --save_table $save_path/orb_plot_$var/trans_table.csv
    evo_res $save_path/orb_${var}_rot --save_table $save_path/orb_plot_$var/rot_table.csv
    evo_res $save_path/orb_${var}_rpe --save_table $save_path/orb_plot_$var/trans_relativ_table.csv
    evo_res $save_path/orb_${var}_rot_rpe --save_table $save_path/orb_plot_$var/rot_relativ_table.csv
done
sleep 0.1s
python ~/awen_evaluation/analyse_awen_ORB3.py $save_path $save_path