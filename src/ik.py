import sympy as sy
from sympy.physics import mechanics as mc
import numpy as np
from sympy import sympify, nsimplify
import math
import rospy
from std_msgs.msg import *
from sensor_msgs.msg import JointState
R,theta, alpha, a, d,theta1, theta2, theta3, theta4, theta5, theta6, theta7,theta8, d1,d3,d5 ,d7= sy.symbols('R,theta, alpha, a, d,theta1, theta2, theta3, theta4, theta5, theta6, theta7,theta8, d1,d3,d5,d7')
pi=np.pi

def rnd(Q):
	round(Q,3)
	if Q>0:
		while Q>(3.14):
			Q=Q-(pi)
	else :
		while Q<-(3.14):
			Q=Q+(pi)
	return round(Q,3)
    	
	
def getqdot(J,xc,yc,zc,xd,yd,zd):
	J_inv=np.linalg.pinv(J)
	Xdot=sy.Matrix([[xd-xc,yd-yc,zd-zc]])
	Xdot=np.array(Xdot,dtype='float')
	Xdot_f=np.zeros((Xdot.shape[0],2*Xdot.shape[1]))
	Xdot_f[:,:3]=Xdot
	Qdot=J_inv@Xdot_f.T
	Qdot=Qdot.T
	Qdot=np.array(Qdot,dtype=float)
	return Qdot

def Inverse_kin(Q,T):
	f=T[:3,3]
	X=[theta1,theta2,theta3,theta4,theta5,theta6]
	J_half=f.jacobian(X)
	J_otherhalf=T0_1[:3,2].row_join(T0_2[:3,2].row_join(T0_3[:3,2].row_join(T0_4[:3,2].row_join(T0_5[:3,2].row_join(T0_6[:3,2])))))
	J=J_half.col_join(J_otherhalf)
	J=J.subs({theta1:Q[0,0],theta2:Q[0,1],theta3:Q[0,2],theta4:Q[0,3],theta5:Q[0,4],theta6:Q[0,5]})
	J=nsimplify(J,tolerance=1e-3,rational=True)
	J=np.array(J,dtype=float)
	return J

if __name__=="__main__":
	
	A = sy.Matrix([[sy.cos(theta), -sy.sin(theta)*sy.cos(alpha), sy.sin(theta)*sy.sin(alpha), a*sy.cos(theta)],
		         [sy.sin(theta), sy.cos(theta)*sy.cos(alpha), -sy.cos(theta)*sy.sin(alpha), a*sy.sin(theta)],
		         [0, sy.sin(alpha), sy.cos(alpha),d],
		         [0, 0, 0, 1]])
	

	A0_1= A.subs({alpha:-pi/2, a:0, theta:theta1, d:355.6}) #0.3556

	A1_2= A.subs({alpha:pi/2, a:0, theta:theta2, d:0})
	A1_2=nsimplify(A1_2,tolerance=1e-3,rational=True)

	A2_3= A.subs({alpha:pi/2, a:0, theta:theta3, d:520.7}) #0.5207
	A2_3=nsimplify(A2_3,tolerance=1e-3,rational=True)

	A3_4= A.subs({alpha:-pi/2, a:0, theta:theta4, d:0})
	A3_4=nsimplify(A3_4,tolerance=1e-3,rational=True)

	A4_5= A.subs({alpha:-pi/2, a:0, theta:theta5, d:520.7}) #1.04394
	A4_5=nsimplify(A4_5,tolerance=1e-3,rational=True)

	A5_6= A.subs({alpha:pi/2, a:0, theta:theta6, d:0})
	A5_6=nsimplify(A5_6,tolerance=1e-3,rational=True)
	
	A6_7= A.subs({alpha:0, a:0, theta:0, d:523.24})
	A6_7=nsimplify(A6_7,tolerance=1e-3,rational=True)
	
	T0_1=A0_1

	T0_2=(A0_1*A1_2)

	T0_3=(T0_2*A2_3)

	T0_4=(T0_3*A3_4)

	T0_5=(T0_4*A4_5)

	T0_6=(T0_5*A5_6)
	
	T0_7=(T0_6*A6_7)
	
	T=T0_6
	d11,d33,d55,d77=355.6,520.7,520.7,523.24
	xd,yd,zd=(523.24+520.7+520.7),0,355.6
	Q=np.zeros(6)
	Q=np.array([0,0,0,0,0,0])
	#print(Q)
	Ta=T.subs({theta1:Q[0],theta2:Q[1],theta3:Q[2],theta4:Q[3],theta5:Q[4],theta6:Q[5]})
	Ta=nsimplify(Ta,tolerance=1e-3,rational=True)
	Ta=np.array(Ta,dtype=float)
	xc,yc,zc=Ta[0,3],Ta[1,3],Ta[2,3]
	print(str(xc-xd) + " " + str(yc-yd) + " " + str(zc-zd)+ " " + str(Ta[0,0]))
	f=T[:3,3]
	X=[theta1,theta2,theta3,theta4,theta5,theta6]
	J_half=f.jacobian(X)
	J_otherhalf=T0_1[:3,2].row_join(T0_2[:3,2].row_join(T0_3[:3,2].row_join(T0_4[:3,2].row_join(T0_5[:3,2].row_join(T0_6[:3,2])))))
	J=J_half.col_join(J_otherhalf)
	J=J.subs({theta1:Q[0],theta2:Q[1],theta3:Q[2],theta4:Q[3],theta5:Q[4],theta6:Q[5]})
	J=nsimplify(J,tolerance=1e-3,rational=True)
	J=np.array(J,dtype=float)
	qd=getqdot(J,xc,yc,zc,xd,yd,zd)
	Q=Q+qd
	
	while (1):
		T=T0_6
		Ta=T.subs({theta1:Q[0,0],theta2:Q[0,1],theta3:Q[0,2],theta4:Q[0,3],theta5:Q[0,4],theta6:Q[0,5]})
		Ta=nsimplify(Ta,tolerance=1e-4,rational=True)
		
		Ta=np.array(Ta,dtype=float)
		xc,yc,zc=Ta[0,3],Ta[1,3],Ta[2,3]
		print(str(xc-xd) + " " + str(yc-yd) + " " + str(zc-zd))
		if (xc==xd and yc==yd and zc==zd):
			print("BREAK")
			break;
		
		J=Inverse_kin(Q,T)
		qd=getqdot(J,xc,yc,zc,xd,yd,zd)
		Q=Q+qd
		#print(Q)
	
	for i in range(0,6):
		Q[0,i]=rnd(Q[0,i])
	
	print(Q)
	
	TD=T0_7.subs({theta1:0,theta2:0,theta3:0,theta4:0,theta5:0,theta6:0})
	TD=nsimplify(TD,tolerance=1e-3,rational=True)
	print(TD)
	TO=T0_7.subs({theta1:Q[0,0],theta2:Q[0,1],theta3:Q[0,2],theta4:Q[0,3],theta5:Q[0,4],theta6:Q[0,5]})
	TO=nsimplify(TO,tolerance=1e-3,rational=True)
	print(TO)
	
