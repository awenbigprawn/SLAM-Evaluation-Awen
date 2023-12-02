#!/bin/bash
pathDatasetEuroc='/home/yuwen/Euroc' #Example, it is necesary to change it by the dataset path
pathORB='/home/yuwen/ORB_SLAM3/ORB_SLAM3/Examples'
name='MH01'
#------------------------------------
# Stereo-Inertial Examples
echo "Launching MH01 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/MH_01_easy ./Stereo-Inertial/EuRoC_TimeStamps/MH01.txt dataset-MH01_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='MH02'
echo "Launching MH02 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/MH_02_easy ./Stereo-Inertial/EuRoC_TimeStamps/MH02.txt dataset-MH02_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='MH03'
echo "Launching MH03 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/MH_03_medium ./Stereo-Inertial/EuRoC_TimeStamps/MH03.txt dataset-MH03_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='MH04'
echo "Launching MH04 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/MH_04_difficult ./Stereo-Inertial/EuRoC_TimeStamps/MH04.txt dataset-MH04_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='MH05'
echo "Launching MH05 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/MH_05_difficult ./Stereo-Inertial/EuRoC_TimeStamps/MH05.txt dataset-MH05_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V101'
echo "Launching V101 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V1_01_easy ./Stereo-Inertial/EuRoC_TimeStamps/V101.txt dataset-V101_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V102'
echo "Launching V102 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V1_02_medium ./Stereo-Inertial/EuRoC_TimeStamps/V102.txt dataset-V102_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V103'
echo "Launching V103 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V1_03_difficult ./Stereo-Inertial/EuRoC_TimeStamps/V103.txt dataset-V103_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V201'
echo "Launching V201 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V2_01_easy ./Stereo-Inertial/EuRoC_TimeStamps/V201.txt dataset-V201_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V202'
echo "Launching V202 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V2_02_medium ./Stereo-Inertial/EuRoC_TimeStamps/V202.txt dataset-V202_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"

name='V203'
echo "Launching V203 with Stereo-Inertial sensor"
./Stereo-Inertial/stereo_inertial_euroc ../Vocabulary/ORBvoc.txt ./Stereo-Inertial/EuRoC.yaml "$pathDatasetEuroc"/V2_03_difficult ./Stereo-Inertial/EuRoC_TimeStamps/V203.txt dataset-V203_stereoi
mkdir "$pathORB"/"$name"
cd "$pathORB"
mv ExecTimeMean.txt f_dataset-"$name"_stereoi.txt kf_dataset-"$name"_stereoi.txt LBA_Stats.txt LocalMapTimeStats.txt SessionInfo.txt TrackingTimeStats.txt TrackLocalMapStats.txt -t "$pathORB"/"$name"
