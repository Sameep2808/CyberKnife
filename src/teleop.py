#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import sys, select, termios, tty

msg = """
Control Your Toy!
---------------------------
Moving around:
  	w

a	s	d

q: Increase Speed
e: Decrease Speed
CTRL-C to quit
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key
    
    
if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub_move = rospy.Publisher('/proj1/f_controller/command', Float64, queue_size=10)
    pub_move1 = rospy.Publisher('/proj1/r_controller/command', Float64, queue_size=10)
    pub_move2 = rospy.Publisher('/proj1/l_controller/command', Float64, queue_size=10) 
    # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    
    speed_f=0;
    speed_r=0;
    speed_l=0;
    count=0;
    s=0;
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'q':
            	s+=5;
            	#print("New Speed ="+(s+50));
            if key == 'q':
            	s-=5;
            	#print("New Speed ="+(s+50));
            if key == 'q':
            	s+=5;
            if key == 'w':
            	speed_f=50+s;
            	speed_r=50+s;
            	speed_l=50+s;
            if key == 's':
            	speed_f=-50-s;
            	speed_r=-50-s;
            	speed_l=-50-s;
            if key == 'd':
            	speed_f=20;
            	speed_r=-30;
            	speed_l=30;
            if key == 'a':
            	speed_f=20;
            	speed_r=30;
            	speed_l=-30;
            elif key == ' ':
            	speed_f=0;
            	speed_r=0;
            	speed_l=0;
            else:
            	count=count+1;
            	if(count>5):
            		speed_f=0;
            		speed_r=0;
            		speed_l=0;
            		count=0;
            		
            	if (key == '\x03'):
            		break

            pub_move.publish((-1)*speed_f)
            pub_move1.publish(speed_r) 
            pub_move2.publish((-1)*speed_l)  # publish the control speed. 
	

    except:
        print("Error");
    
    
    finally:
        pub_move.publish(speed_f)
        pub_move1.publish(speed_r) 
        pub_move2.publish(speed_l)
        # twist = Twist()
        # twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        # twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
