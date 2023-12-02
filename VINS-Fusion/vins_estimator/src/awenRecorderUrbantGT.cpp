#include "ros/ros.h"
#include <nav_msgs/Path.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/NavSatFix.h>
#include <iostream>
#include <fstream>



void pose_graph_pathCallback(const nav_msgs::Odometry::ConstPtr &odometry_msg)
{
    std::ofstream foutC("./Urbant_rosbag/gps_groundtruth.csv", std::ios::app);
    
    foutC.setf(std::ios::fixed, std::ios::floatfield);
    foutC.precision(0);
    foutC << odometry_msg->header.stamp.toSec() * 1e9 << ",";
    foutC.precision(5);
    foutC << odometry_msg->pose.pose.position.x << ","
            << odometry_msg->pose.pose.position.y << ","
            << odometry_msg->pose.pose.position.z << ","
            << odometry_msg->pose.pose.orientation.x << ","
            << odometry_msg->pose.pose.orientation.y << ","
            << odometry_msg->pose.pose.orientation.z << ","
            << odometry_msg->pose.pose.orientation.w << std::endl;
    foutC.close();
}

void awenGpsCallback(const sensor_msgs::NavSatFix::ConstPtr &gps_msg)
{
    std::ofstream foutC("./Urbant_rosbag/gps_groundtruth_NavSatFix.csv", std::ios::app);
    
    foutC.setf(std::ios::fixed, std::ios::floatfield);
    foutC.precision(0);
    foutC << gps_msg->header.stamp.toSec() * 1e9 << ",";
    foutC.precision(7);
    foutC << gps_msg->latitude << ","
            << gps_msg->longitude << ","
            << gps_msg->altitude << std::endl;
    foutC.close();
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "awenRecorderUrbantGT");
    ros::NodeHandle n("~");

    ros::Subscriber sub_pose_graph_path = n.subscribe("/vo", 100, pose_graph_pathCallback);
    ros::Subscriber sub_gps = n.subscribe("/ublox_gps/fix", 100, awenGpsCallback);
    ros::spin();
    return 0;
}