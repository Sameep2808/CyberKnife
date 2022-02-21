# CyberKnife
## Badges
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Authors
- [Sameep Pote](https://github.com/Sameep2808) - Graduate student at University of Maryland pursuing M.Eng. Robotics.Loves to watch animes.
- [Atharva Paralikar](https://github.com/Atharva-Paralikar) - Graduate student at University of Maryland.
## License
```
MIT License

Copyright (c) 2021 Sameep Pote, Atharva Paralikar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Overview

## Dependencies and Technologies used

- Programming language : C++
- Build system : catkin_make
- Operating System : Ubuntu 20.04
- Packages : sensor_msgs, gazebo_msgs

## Working

## CAD Model
The robot was designed using SolidWorks. The configuration of joints was inspired from a real
CyberKnife robot. The parts were designed and assembled with comparable dimensions of a real
CyberKnife. The URDF was created using the SW2URDF utility. Special care was taken while assigning
the coordinate frame at each joint. The exported URDF meshes of the Robot and the URDF file were
further used for simulation in Gazebo. The tool outputs all the necessary folders and files to
launch the robot in an empty world.

![pic1](https://github.com/Sameep2808/CyberKnife/blob/main/pics/Screenshot%20from%202022-02-20%2019-49-17.png)

## Denavit-Hartenberg Parameters
![pic2](https://github.com/Sameep2808/CyberKnife/blob/main/pics/Screenshot%20from%202022-02-20%2019-52-56.png)
![pic3](https://github.com/Sameep2808/CyberKnife/blob/main/pics/Screenshot%20from%202022-02-20%2019-53-14.png)

## Control Methods
Control Methods used in our project for controlling all the joins of the CyberKnife are Joint Position
Controller from effort controllers and Joint State Controller. The Joint Position Controller commands a
desired position to the joint. The position is controlled using PID control to specify the effort to the joint.
When started, the controller will command to the current position. The joint state controller is used to
simulate the prototype in Rviz using the joint state publisher GUI. Using it makes studying the workspace
of the robot easy as we can manually control individual joints through a simple slider GUI. For autonomous
working of the robot, we use the Joint Position controller as its command sends the respective joints at
desired position and stabilizes over there using the built-in PID controller in the effort controller.
![pic4](https://github.com/Sameep2808/CyberKnife/blob/main/pics/Screenshot%20from%202022-02-20%2019-54-17.png)

## Gazebo and Rviz Visualization
The following Images represent Rviz and Gazebo Visualization using LiDAR. The red line in Rviz
represents that the LiDAR has successfully detected an object in front of the arm and the node terminal on
the right shows the exact location of the detected object.
![pic5](https://github.com/Sameep2808/CyberKnife/blob/main/pics/Screenshot%20from%202022-02-20%2019-55-01.png)

## Application
The project revolves around designing and simulating a CyberKnife. CyberKnife is 
a non-surgical Robotic Radiosurgery system that destroys tumors using highly precise, 
targeted radiation, with minimal damage to surrounding healthy tissue. Unlike traditional 
radiation therapy that can take multiple sessions, this therapy is complete in fewer 
sessions. This therapy is as effective as other radiation therapies but without the side 
effects. This is a simple painless process and patients can resume normal activity almost
immediately. Surgical Robots have gained prominence in recent years due to their accuracy,
repeatability, and robustness. Cyber-Knife used in radio surgery has numerous advantages
hence studying it is necessary and important. Due to the need of multiple orientations, this 
problem is a good lesson in handling such real-world problems. This application requires us 
to design a manipulator to be able to fire the laser beam at a particular point in space 
from multiple orientations.



## Problems Faced and Mitigation
The following are the problems faced by us during the execution of the given project:
1. While launching the URDF file in Gazebo world we observed that at a default inertia and friction
without the joint state controller the arm used to collapse.
2. The YD LiDAR used was a 3D LiDAR hence gave multiple distance values and not the center of
the object
3. Problems faced launching Joint State Publisher GUI



## Steps to Build package
1. Create Catkin Workspace
```
cd ~/catkin_ws
catkin_make clean && catkin_make
```
2. Copy the repository in src folder of catkin workspace
```
git clone https://github.com/Sameep2808/CyberKnife.git
cd ..
catkin_make clean && catkin_make
source ./devel/setup.bash
```
## Steps to Run package
1. Make sure you have sourced setup file
```
cd ~/catkin_ws
source ./devel/setup.bash
```

2. To run the package 
```
roslaunch gas navigation.launch
```


## Making Doxygen documentation

This generates a index.html page in the build/coverage sub-directory that can be viewed locally in a web browser.
How to Generate Doxygen Documentation

To install doxygen run the following command:
```
sudo apt-get install doxygen

Now from the cloned directory run:

doxygen doxygen
```
Generated doxygen files are in html format and you can find them in ./docs folder. With the following command
```
cd docs
cd html
google-chrome index.html
```
## Working with Eclipse IDE

### Installation

In your Eclipse workspace directory (or create a new one), checkout the repo (and submodules)
```
mkdir -p ~/workspace
cd ~/workspace
git clone --recursive https://github.com/Sameep2808/gas.git
```

In your work directory, use cmake to create an Eclipse project for an [out-of-source build] of cpp-boilerplate

```
cd ~/workspace
mkdir -p boilerplate-eclipse
cd boilerplate-eclipse
cmake -G "Eclipse CDT4 - Unix Makefiles" -D CMAKE_BUILD_TYPE=Debug -D CMAKE_ECLIPSE_VERSION=4.7.0 -D CMAKE_CXX_COMPILER_ARG1=-std=c++14 ../cpp-boilerplate/
```

### Import

Open Eclipse, go to File -> Import -> General -> Existing Projects into Workspace -> 
Select "boilerplate-eclipse" directory created previously as root directory -> Finish

### Edit

Source files may be edited under the "[Source Directory]" label in the Project Explorer.


## Build

To build the project, in Eclipse, unfold boilerplate-eclipse project in Project Explorer,
unfold Build Targets, double click on "all" to build all projects.

### Run

1. In Eclipse, right click on the boilerplate-eclipse in Project Explorer,
select Run As -> Local C/C++ Application

2. Choose the binaries to run (e.g. shell-app, cpp-test for unit testing)


### Debug


1. Set breakpoint in source file (i.e. double click in the left margin on the line you want 
the program to break).

2. In Eclipse, right click on the boilerplate-eclipse in Project Explorer, select Debug As -> 
Local C/C++ Application, choose the binaries to run (e.g. shell-app).

3. If prompt to "Confirm Perspective Switch", select yes.

4. Program will break at the breakpoint you set.

5. Press Step Into (F5), Step Over (F6), Step Return (F7) to step/debug your program.

6. Right click on the variable in editor to add watch expression to watch the variable in 
debugger window.

7. Press Terminate icon to terminate debugging and press C/C++ icon to switch back to C/C++ 
perspetive view (or Windows->Perspective->Open Perspective->C/C++).


### Plugins

- CppChEclipse

    To install and run cppcheck in Eclipse

    1. In Eclipse, go to Window -> Preferences -> C/C++ -> cppcheclipse.
    Set cppcheck binary path to "/usr/bin/cppcheck".

    2. To run CPPCheck on a project, right click on the project name in the Project Explorer 
    and choose cppcheck -> Run cppcheck.


- Google C++ Sytle

    To include and use Google C++ Style formatter in Eclipse

    1. In Eclipse, go to Window -> Preferences -> C/C++ -> Code Style -> Formatter. 
    Import [eclipse-cpp-google-style][reference-id-for-eclipse-cpp-google-style] and apply.

    2. To use Google C++ style formatter, right click on the source code or folder in 
    Project Explorer and choose Source -> Format

[reference-id-for-eclipse-cpp-google-style]: https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-cpp-google-style.xml

- Git

    It is possible to manage version control through Eclipse and the git plugin, but it typically requires creating another project. If you're interested in this, try it out yourself and contact me on Canvas.
