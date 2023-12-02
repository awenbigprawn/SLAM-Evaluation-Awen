This bachelor thesis is a project to evaluate the three SLAM libraries---VINS FUSION, Kimera, ORB-SLAM3. I have made some small changes in the original code of each library to record the trajectory and the time usage easier.

# 1. VINS FUSION
The dictionary 'VINS-Fusion' is for VINS FUSION. Put the dictionary in catkin workspace of ROS environment and build it with the instructions from the [original website of VINS FUSION](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion).

To test it and record the time usage and the trajectory, a result dictionary named 'vins_result' must be first made.
 ```
    mkdir ~/vins_result
 ```
Then test the library:
## 1.1 for EuRoC datasets
Each command line must be executed in an independent terminal:
 ```
    roslaunch vins vins_rviz.launch
    rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml 
    rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/euroc/euroc_stereo_imu_config.yaml
    rosrun vins awen_evaluate
    rosbag play --clock YOUR_DATASET_FOLDER/your_euroc_rosbag.bag
 ```
## 1.2 for UrbANT datasets
Each command line must be executed in an independent terminal:
 ```
    roslaunch vins vins_rviz.launch
    rosrun vins vins_node ~/catkin_ws/src/VINS-Fusion/config/Urbant/urbant_stereo_imu_config.yaml 
    rosrun loop_fusion loop_fusion_node ~/catkin_ws/src/VINS-Fusion/config/Urbant/urbant_stereo_imu_config.yaml
    rosrun vins awen_evaluate
    rosbag play YOUR_DATASET_FOLDER/your_urbant_rosbag.bag
 ```
After the test, all the needed result files are in the dictionary '~/vins_result':

- The 'pose_graph_path.csv' records the trajectory after loop closure optimization.
- The 'vins_estimator_path.csv' records the trajectory without loop closure optimization.
- The 'trackImage_time.csv' records the front-end time usage.

# 2. Kimera
The dictionaries 'Kimera-VIO-ROS' and 'Kimera-VIO' are for Kimera. First, install and build the Kimera library from the [original website of Kimera-VIO-ROS](https://github.com/MIT-SPARK/Kimera-VIO-ROS). Then, clone and replace the original Kimera-VIO-ROS and Kimera-VIO dictionaries with the dictionaries in slam-evaluation-awen. Finally, build the catkin workspace again.
 ```
    cd catkin_ws
    catkin build
 ```
When the installation is finished, we can test the library:
## 2.1 for EuRoC dataset
Each command line must be executed in an independent terminal:
 ```
    roslaunch kimera_vio_ros kimera_vio_ros_euroc.launch
    rviz -d $(rospack find kimera_vio_ros)/rviz/kimera_vio_euroc.rviz
    rosbag play --clock YOUR_DATASET_FOLDER/your_euroc_rosbag.bag
 ```
## 2.2 for UrbANT dataset
Each command line must be executed in an independent terminal:
 ```
    roslaunch kimera_vio_ros kimera_vio_ros_urbant.launch
    rviz
    rosbag play --clock YOUR_DATASET_FOLDER/your_urbant_rosbag.bag
 ```
After the test, all the needed result files are in the dictionary 'Kimera-VIO-ROS/output_logs/(Dataset)':
- The 'traj_pgo.csv' records the trajectory after pose graph optimization.
- The 'traj_vio.csv' records the trajectory without pose graph optimization.
- The 'output_frontend_stats.csv' records the front-end time usage.

# 3. ORB SLAM3
Delete or comment the line `source path_to_your_catkin_ws/devel/setup.bash` in .bashrc file, then install the ORB-SLAM3 with the provided dictionary 'ORB_SLAM3' in slam-evaluation-awen by following the instructions from the [original website of ORB SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3).

## 3.1 for EuRoC dataset
Each command line must be executed in an independent terminal:
 ```
    roscore
    rosrun ORB_SLAM3 Stereo_Inertial /Path/to/ORB_SLAM3/Vocabulary/ORBvoc.txt /Path/to/ORB_SLAM3/Examples/Stereo-Inertial/EuRoC.yaml true
    rviz
    rosbag play --clock YOUR_DATASET_FOLDER/your_euroc_rosbag.bag
 ```
## 3.2 for UrbANT dataset
Each command line must be executed in an independent terminal:
 ```
    roscore
    rosrun ORB_SLAM3 Stereo_Inertial /Path/to/ORB_SLAM3/Vocabulary/ORBvoc.txt /Path/to/ORB_SLAM3/Examples/Stereo-Inertial/Urbant.yaml true
    rviz
    rosbag play --clock YOUR_DATASET_FOLDER/your_urbant_rosbag.bag /imu/data:=/imu /zed2/zed_node/left/image_rect_gray:=/camera/left/image_raw /zed2/zed_node/right/image_rect_gray:=/camera/right/image_raw
 ```
After the test, all the needed result files are at under 'Home' of the Linux system:
- The 'traj_pgo.csv' records the trajectory.
- The 'output_frontend_stats.csv' records the front-end time usage.

# 4. gps_umd
This is a module that can help to translate the gps message NavSatFix.msg into Odometry.msg, which is easier to be recorded into a .csv file. Copy the dictionary into catkin workspace of your ROS and build it for installation. Edit the launchfile in 'gps_umd/gps_common/launch/utm_odometry_node.launch' first, then use it in ROS with command:

  ```
  roslaunch gps_common utm_odometry_node.launch
  ```
Open another terminal, use the ros node 'awen_UrbantGT' in VINS FUSION to record the gps trajectory of an UrbANT dataset. Before using, a dictionary must be created:
  ```
  mkdir ./Urbant_rosbag
  ```
then record the GPS groundtruth trajectory:
  ```
  rosrun vins awen_UrbantGT
  ```
When the test finished, the recorded GPS groundtruth trajectory is saved in file 'gps_groundtruth.csv' in dictionary 'Urbant_rosbag'.

# 5. evo
evo is the evaluation model to calculate the ATE and ARE. The instructions for installation and using are in the [original website of evo](https://github.com/MichaelGrupp/evo).

# 6. awen_scripts
Here are some .sh file to save time of write commands in terminal.


# 7. awen_evaluation 
awen_evaluation includes many tools to plot the localization accuracy results and put the results from different datasets in one .csv file.
analyse_awen_slamName.py are the main files to put results together.

