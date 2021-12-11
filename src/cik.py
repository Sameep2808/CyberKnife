import sympy as sy
from sympy.physics import mechanics as mc
from numpy import *
import numpy as np
from sympy import sympify, nsimplify
import math
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import JointState
import sys, select, termios, tty
t1,t2,t3= sy.symbols('t1,t2,t3')
pi=np.pi

msg = """
Control Cyberr Knife!

w = Next Step
s = Previous Step
q = Increase Step Size
a = Decrease Step Size
z = Reset the Steps to 0
e = Get new co-ordinates from the LiDAR 

CTRL-C to quit
"""

pub_c1 = rospy.Publisher('/finalec/c1/command', Float64, queue_size=10)
pub_c2 = rospy.Publisher('/finalec/c2/command', Float64, queue_size=10)
pub_c3 = rospy.Publisher('/finalec/c3/command', Float64, queue_size=10)
pub_c4 = rospy.Publisher('/finalec/c4/command', Float64, queue_size=10)
pub_c5 = rospy.Publisher('/finalec/c5/command', Float64, queue_size=10)


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def map(x,imin,imax,omin,omax):
	return (((x-imin) * (omax-omin)) / (imax-imin))+omin

def ikk(x,y,z,phi,e):
	a1= 690
	a2 = 690
	a3 = 175
	
	theta_0=math.atan2(y,x)
	
	px = sqrt(x**2 + y**2)
	py = z

	
	phi = deg2rad(phi)


	wx = px - a3*cos(phi)
	wy = py - a3*sin(phi)

	delta = wx**2 + wy**2
	c2 = ( delta -a1**2 -a2**2)/(2*a1*a2)
	s2 = sqrt(1-(c2**2))  # elbow down
	theta_2 = arctan2(s2, c2)

	s1 = ((a1+a2*c2)*wy - a2*s2*wx)/delta
	c1 = ((a1+a2*c2)*wx + a2*s2*wy)/delta
	theta_1 = arctan2(s1,c1)
	theta_3 = phi-theta_1-theta_2
	#print('theta_1: ', rad2deg(theta_0))
	#print('theta_1: ', rad2deg(theta_1))
	#print('theta_2: ', rad2deg(theta_2))
	#print('theta_3: ', rad2deg(theta_3))
	#print('theta_1: ', (theta_0))
	#print('theta_1: ', (theta_1))
	#print('theta_2: ', (theta_2))
	#print('theta_3: ', (theta_3))
	pub_c1.publish(theta_0)
	pub_c2.publish(theta_1)
	pub_c3.publish(theta_2)
	pub_c4.publish(theta_3)
	print(rad2deg(e))
	print(rad2deg(theta_0))
	if(rad2deg(theta_0) > 45):
		pub_c5.publish(e-theta_0)
	if(round(rad2deg(theta_0),2) == 45):
		pub_c5.publish(e-theta_0)
	if(rad2deg(theta_0) < 45):
		pub_c5.publish(-(-e+theta_0))
	

def gcor(x,y,z,t):
	x1=[[0,0,0],[0,0,0]]
	x1[0][0]=x-700*cos(deg2rad(t))
	x1[1][0]=y-700*sin(deg2rad(t))
	#print(x1[0][0])
	#print(x1[1][0])
	return x1

def callback(msg):
	global xd,yd
	for i in range(360,700):
		if(msg.ranges[i]<=2):
			xd=0.4-msg.ranges[i]*cos(deg2rad(i/4))
			yd=0+msg.ranges[i]*sin(deg2rad(i/4))
	
	
if __name__=="__main__":
	rospy.init_node('cik1')
	settings = termios.tcgetattr(sys.stdin)
	a,s,x,y,z=0,45,1000,1000,400
	global xd,yd
	xd,yd=0,0
	rate = rospy.Rate(10)
	print(msg)
	while not rospy.is_shutdown():
		rate.sleep()
		sub = rospy.Subscriber('/laser/scan', LaserScan, callback)
		key = getKey()
		if key == 'w':
			if a<0 or a>90:
				a=0
			c=gcor(x,y,z,a)
			p=(arctan2((y-c[1][0]),(x-c[0][0])))
			ikk(c[0][0],c[1][0],z,90,p)
			a=a+s
			#print("phi =",90)
			print("Next angle =",a)
		if key == 's':
			if a<0 or a>90:
				a=0
			c=gcor(x,y,z,a)
			pd=sqrt((y-c[1][0])**2 + (x-c[0][0])**2)
			cp=arccos(pd/700)
			sp = sqrt(1-(cp**2))
			p=rad2deg(arctan2(sp,cp))
			ikk(c[0][0],c[1][0],z,90,(2*p)-90)
			a=a-s
			print("Next angle =",a)
			print(a)
		if key == 'z':
			a=0
		if key == 'q':
			a=a-s
			s=s+1
			print("Step size =",s)
		if key == 'e':
			x,y=1000*yd,1000*xd
			print("x =",x)
			print("y =",y)
		if key == 'a':
			a=a-s
			s=s-1
			print("Step size =",s)
		if (key == '\x03'):
			break

		
