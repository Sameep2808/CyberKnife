#include <iostream>
#include <cmath>
#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/LaserScan.h"
#include <sstream>
double angle[4] = { 0, 0, 0, 0 };
double rad = M_PI / 180;

void ik_solve(double x,double y,double z, int phi) {
  
  double length[3] = { 690, 690, 175 };
	
  angle[0] = atan2(y,x) /rad;
  
  double d=abs(sqrt((x*x)+(y*y)));
  
  double x2 = d - (length[2] * cos(rad * phi));
  double y2 = z - (length[2] * sin(rad * phi));
  double delta = (x2*x2)+(y2*y2);
  
  double c2=(delta - (length[0]*length[0]) - (length[1]*length[1]))/(2*length[1]*length[0]);
  double s2=sqrt(1-(c2*c2));
  
  if(c2==0)
  angle[2] = (atan2(s2,c2))/rad;
  else
  angle[2] = (atan(s2/c2))/rad;
 
     
              
  double c1 = ((((length[0] + (length[1] * cos(angle[2]))) * x2)
      + (length[1] * y2 * sin(angle[2]))) / ((x2 * x2) + (y2 * y2)));
  double s1 = ((((length[0] + (length[1] * cos(angle[2]))) * y2)
      - (length[1] * x2 * sin(angle[2]))) / ((x2 * x2) + (y2 * y2)));
  
  angle[1] = (atan2(s1,c1))/rad;
  
  angle[3] = (phi) - (angle[1] + angle[2]);
  std::cout << angle[0] << std::endl;
  std::cout << angle[1] << std::endl;
  std::cout << angle[2] << std::endl;
  std::cout << angle[3] << std::endl;
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "iks");
  ros::NodeHandle n;
  ros::Publisher c1_pub = n.advertise<std_msgs::Float64>("/finalec/c1/command", 50);
  ros::Publisher c2_pub = n.advertise<std_msgs::Float64>("/finalec/c2/command", 50);
  ros::Publisher c3_pub = n.advertise<std_msgs::Float64>("/finalec/c3/command", 50);
  ros::Publisher c4_pub = n.advertise<std_msgs::Float64>("/finalec/c4/command", 50);
  ros::Publisher c5_pub = n.advertise<std_msgs::Float64>("/finalec/c5/command", 50);
  ik_solve(1000,0,-100,-90);
  std_msgs::Float64 m1;
  std_msgs::Float64 m2;
  std_msgs::Float64 m3;
  std_msgs::Float64 m4;
  std_msgs::Float64 m5;
  m1.data = angle[0]*rad;
  m2.data = -angle[1]*rad;
  m3.data = -angle[2]*rad;
  m4.data = -angle[3]*rad;
  m5.data = 0;
  ros::Rate loop_rate(1);
  while (ros::ok()){
  c1_pub.publish(m1);
  c2_pub.publish(m2);
  c3_pub.publish(m3);
  c4_pub.publish(m4);
  c5_pub.publish(m5);
  ros::spinOnce();
  loop_rate.sleep();}

  return 0;
}
