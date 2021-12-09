///============================================================================
/// @file        : sub.cpp
/// @version     : 1.0
/// @author      : Sameep Pote
/// @copyright   : MIT License
/// @brief       : sub.cpp This file is used to receive the custom string
///============================================================================
#include <math.h> 
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/LaserScan.h"

#define PI 3.14159265

int k = 0;
double x,y;
ros::Publisher pub;
void chatterCallback(const sensor_msgs::LaserScan::ConstPtr &data) {
  //ROS_INFO("At Size: [%ld]", (data -> ranges).size());
  //ROS_INFO("At 0: [%f]", (data -> ranges[0]));
  //ROS_INFO("At 90: [%f]", (data -> ranges[360]));
  //ROS_INFO("At 180: [%f]", (data -> ranges[719]));
  while(k<5)
  	{
  	for(int i=0; i<360; i++)
  {
  	if(data -> ranges[i]<=2)
  	{
  		x += (data -> ranges[i])*cos((i/4)*(PI/180.0));
  		y += (data -> ranges[i])*sin((i/4)*(PI/180.0));
  	}
  }
  for(int i=0; i<720; i++)
  {
  	if(data -> ranges[i]<=2)
  	{
  		y += (data -> ranges[i])*cos(((i-360)/4)*(PI/180.0));
  		x += -(data -> ranges[i])*sin(((i-360)/4)*(PI/180.0));
  	}
  }
  k++;
  }
  ROS_INFO("At x,y: [%f, %f]", x/(5*720),y/(5*720));
  	
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "detect");

  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("/laser/scan", 1, chatterCallback);
  ros::Rate loop_rate(10);
  ros::spin();

  return 0;
}
