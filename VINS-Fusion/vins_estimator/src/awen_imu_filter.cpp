#include "ros/ros.h"
#include <sensor_msgs/Imu.h>
#include <sensor_msgs/Image.h>
#include <iostream>
#include <fstream>


class SubscribeAndPublish
{
public:
  SubscribeAndPublish()
  {
    ROS_INFO("SubscribeAndPublish is created!");
    foutC = std::ofstream("./Urbant_rosbag/imu_urbant.csv", std::ios::out);
    foutC << "timestamp,a_x,a_y,a_z,w_x,w_y,w_z,q_x,q_y,q_z,q_w"<< std::endl;
    foutCimg = std::ofstream("./Urbant_rosbag/img0_IMU.csv", std::ios::out);
    foutCimg << "timestampImgLeft,timestampIMU"<< std::endl;
    foutCimg1 = std::ofstream("./Urbant_rosbag/img1_IMU.csv", std::ios::out);
    foutCimg1 << "timestampImgRight,timestampIMU"<< std::endl;
    //Topic you want to publish
    pub_ = n_.advertise<sensor_msgs::Imu>("/imu0", 10);
    pubImg_ = n_.advertise<sensor_msgs::Image>("/cam0/image_raw", 10);
    pubImg1_ = n_.advertise<sensor_msgs::Image>("/cam1/image_raw", 10);
 
    //Topic you want to subscribe
    sub_ = n_.subscribe("/imu/data", 10, &SubscribeAndPublish::callback, this);
    subImg_ = n_.subscribe("/zed2/zed_node/left/image_rect_gray", 10, &SubscribeAndPublish::callbackimg, this);
    subImg1_ = n_.subscribe("/zed2/zed_node/right/image_rect_gray", 10, &SubscribeAndPublish::callbackimg1, this);
  }
 
  void callback(const sensor_msgs::ImuConstPtr &input_imu_msg)
  {
    int sec = input_imu_msg->header.stamp.sec;
    int nsec = input_imu_msg->header.stamp.nsec;

    foutC.setf(std::ios::fixed, std::ios::floatfield);
    foutC.precision(5);
    foutC << input_imu_msg->header.stamp.toSec() << ",";
    foutC << input_imu_msg->linear_acceleration.x << ","
          << input_imu_msg->linear_acceleration.y << ","
          << input_imu_msg->linear_acceleration.z << ","
          << input_imu_msg->angular_velocity.x << ","
          << input_imu_msg->angular_velocity.y << ","
          << input_imu_msg->angular_velocity.z << ","
          << input_imu_msg->orientation.x << ","
          << input_imu_msg->orientation.y << ","
          << input_imu_msg->orientation.z << ","
          << input_imu_msg->orientation.w << "," << std::endl;
    

    if((nsec>last_timestamp_nsec && sec==last_timestamp_sec)||(sec>last_timestamp_sec)){
      pub_.publish(input_imu_msg);
      ROS_INFO("if is true!---");
    }
    else{
      sensor_msgs::Imu output_imu_msg;
      output_imu_msg.header = input_imu_msg->header;
      output_imu_msg.orientation = input_imu_msg->orientation;
      output_imu_msg.orientation_covariance = input_imu_msg->orientation_covariance;
      output_imu_msg.angular_velocity = input_imu_msg->angular_velocity;
      output_imu_msg.angular_velocity_covariance = input_imu_msg->angular_velocity_covariance;
      output_imu_msg.linear_acceleration = input_imu_msg->linear_acceleration;
      output_imu_msg.linear_acceleration_covariance = input_imu_msg->linear_acceleration_covariance;

      output_imu_msg.header.stamp.nsec = last_timestamp_nsec + 1e7;
      if(output_imu_msg.header.stamp.nsec >= 1e9){
        output_imu_msg.header.stamp.sec += 1;
        output_imu_msg.header.stamp.nsec -= 1e9;
      }
      pub_.publish(output_imu_msg);
      sec=output_imu_msg.header.stamp.sec;
      nsec=output_imu_msg.header.stamp.nsec;
      ROS_INFO("IMU: if is false!--- t = %d.%d",sec,nsec);
    }
    last_timestamp_sec = sec;
    last_timestamp_nsec = nsec;
    return;
  }
 
  void callbackimg(const sensor_msgs::ImageConstPtr &input_img_msg){
    int secImg = input_img_msg->header.stamp.sec;
    int nsecImg = input_img_msg->header.stamp.nsec;

    foutCimg.setf(std::ios::fixed, std::ios::floatfield);
    foutCimg << input_img_msg->header.stamp.toSec()<<","
             << last_timestamp_sec << "." << last_timestamp_nsec << std::endl;
    
    if((nsecImg>last_timestamp_nsecImg && secImg==last_timestamp_secImg)||(secImg>last_timestamp_secImg)){
      pubImg_.publish(input_img_msg);
      ROS_INFO("if is true!---");
    }
    else{
      sensor_msgs::Image output_img_msg;
      output_img_msg.header = input_img_msg->header;
      output_img_msg.height = input_img_msg->height;
      output_img_msg.width = input_img_msg->width;
      output_img_msg.encoding = input_img_msg->encoding;
      output_img_msg.is_bigendian = input_img_msg->is_bigendian;
      output_img_msg.step = input_img_msg->step;
      output_img_msg.data = input_img_msg->data;

      output_img_msg.header.stamp.nsec = last_timestamp_nsec + 6.6667e7;
      if(output_img_msg.header.stamp.nsec >= 1e9){
        output_img_msg.header.stamp.sec += 1;
        output_img_msg.header.stamp.nsec -= 1e9;
      }
      pubImg_.publish(output_img_msg);
      secImg=output_img_msg.header.stamp.sec;
      nsecImg=output_img_msg.header.stamp.nsec;
      ROS_INFO("Img0: if is false!--- t = %d.%d",secImg,nsecImg);
    }
    last_timestamp_secImg = secImg;
    last_timestamp_nsecImg = nsecImg;
    return;
    
  }

  void callbackimg1(const sensor_msgs::ImageConstPtr &input_img1_msg){
    int secImg1 = input_img1_msg->header.stamp.sec;
    int nsecImg1 = input_img1_msg->header.stamp.nsec;

    foutCimg1.setf(std::ios::fixed, std::ios::floatfield);
    foutCimg1 << input_img1_msg->header.stamp.toSec()<<","
             << last_timestamp_sec << "." << last_timestamp_nsec << std::endl;
    
    if((nsecImg1>last_timestamp_nsecImg1 && secImg1==last_timestamp_secImg1)||(secImg1>last_timestamp_secImg1)){
      pubImg1_.publish(input_img1_msg);
      ROS_INFO("if is true!---");
    }
    else{
      sensor_msgs::Image output_img1_msg;
      output_img1_msg.header = input_img1_msg->header;
      output_img1_msg.height = input_img1_msg->height;
      output_img1_msg.width = input_img1_msg->width;
      output_img1_msg.encoding = input_img1_msg->encoding;
      output_img1_msg.is_bigendian = input_img1_msg->is_bigendian;
      output_img1_msg.step = input_img1_msg->step;
      output_img1_msg.data = input_img1_msg->data;//TODO

      output_img1_msg.header.stamp.nsec = last_timestamp_nsecImg1 + 6.6667e7;
      if(output_img1_msg.header.stamp.nsec >= 1e9){
        output_img1_msg.header.stamp.sec += 1;
        output_img1_msg.header.stamp.nsec -= 1e9;
      }
      pubImg1_.publish(output_img1_msg);
      secImg1=output_img1_msg.header.stamp.sec;
      nsecImg1=output_img1_msg.header.stamp.nsec;
      ROS_INFO("Img1: if is false!--- t = %d.%d",secImg1,nsecImg1);
    }
    last_timestamp_secImg1 = secImg1;
    last_timestamp_nsecImg1 = nsecImg1;
    return;
    
  }

private:
  ros::NodeHandle n_; 
  ros::Publisher pub_;
  ros::Publisher pubImg_;
  ros::Publisher pubImg1_;
  ros::Subscriber sub_;
  ros::Subscriber subImg_;
  ros::Subscriber subImg1_;
  int last_timestamp_sec = 0;
  int last_timestamp_nsec = 0;
  int last_timestamp_secImg = 0;
  int last_timestamp_nsecImg = 0;
  int last_timestamp_secImg1 = 0;
  int last_timestamp_nsecImg1 = 0;
public:
  std::ofstream foutC;
  std::ofstream foutCimg;
  std::ofstream foutCimg1;
};


int main(int argc, char **argv)
{
  
  //Initiate ROS
  ros::init(argc, argv, "awen_imu_filter");
 
  //Create an object of class SubscribeAndPublish that will take care of everything
  SubscribeAndPublish SAPObject;
 
  ros::spin();

  SAPObject.foutC.close();
 
  return 0;
}