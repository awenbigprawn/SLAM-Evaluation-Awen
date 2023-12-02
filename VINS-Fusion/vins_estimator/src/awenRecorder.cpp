#include "ros/ros.h"
#include <nav_msgs/Path.h>
#include <nav_msgs/Odometry.h>
#include <iostream>
#include <fstream>



void pose_graph_pathCallback(const nav_msgs::Path::ConstPtr &pose_msg)
{
    std::ofstream foutC("./vins_result/pose_graph_path.csv", std::ios::out);
    for(std::vector<geometry_msgs::PoseStamped>::const_iterator it= pose_msg->poses.begin(); it!= pose_msg->poses.end();  ++it)
          {
            foutC.setf(std::ios::fixed, std::ios::floatfield);
            foutC.precision(0);
            foutC << it->header.stamp.toSec() * 1e9 << ",";
            foutC.precision(5);
            foutC << it->pose.position.x << ","
                    << it->pose.position.y << ","
                    << it->pose.position.z << ","
                    << it->pose.orientation.x << ","
                    << it->pose.orientation.y << ","
                    << it->pose.orientation.z << ","
                    << it->pose.orientation.w << std::endl;
           }
    foutC.close();
}

void vins_estimator_pathCallback(const nav_msgs::Path::ConstPtr &pose_msg)
{
    std::ofstream foutC("./vins_result/vins_estimator_path.csv", std::ios::out);
    for(std::vector<geometry_msgs::PoseStamped>::const_iterator it= pose_msg->poses.begin(); it!= pose_msg->poses.end();  ++it)
          {
            foutC.setf(std::ios::fixed, std::ios::floatfield);
            foutC.precision(0);
            foutC << it->header.stamp.toSec() * 1e9 << ",";
            foutC.precision(5);
            foutC << it->pose.position.x << ","
                    << it->pose.position.y << ","
                    << it->pose.position.z << ","
                    << it->pose.orientation.x << ","
                    << it->pose.orientation.y << ","
                    << it->pose.orientation.z << ","
                    << it->pose.orientation.w << std::endl;
           }
    foutC.close();
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "awenRecorder");
    ros::NodeHandle n("~");
    

    ros::Subscriber sub_pose_graph_path = n.subscribe("/loop_fusion/pose_graph_path", 100, pose_graph_pathCallback);
    ros::Subscriber sub_vins_estimator_path = n.subscribe("/vins_estimator/path", 100, vins_estimator_pathCallback);
    ros::spin();
    return 0;
}