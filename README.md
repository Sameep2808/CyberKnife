# CyberKnife
## Badges
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Authors
- [Sameep Pote](https://github.com/Sameep2808) - Graduate student at University of Maryland pursuing M.Eng. Robotics.Loves to watch animes.
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


##Application
The project revolves around designing and simulating a CyberKnife. CyberKnife is a non-surgical Robotic Radiosurgery system that destroys tumors using highly precise, targeted radiation, with minimal damage to surrounding healthy tissue. Unlike traditional radiation therapy that can take multiple sessions, this therapy is complete in fewer sessions. This therapy is as effective as other radiation therapies but without the side effects. This is a simple painless process and patients can resume normal activity almost immediately. Surgical Robots have gained prominence in recent years due to their accuracy, repeatability, and robustness. Cyber-Knife used in radio surgery has numerous advantages hence studying it is necessary and important. Due to the need of multiple orientations, this problem is a good lesson in handling such real-world problems. This application requires us to design a manipulator to be able to fire the laser beam at a particular point in space from multiple orientations.


## Downloading the turtlebot3 package 
1. In new terminal
```
cd ~/catkin_ws/src/
git clone https://github.com/Sameep2808/CyberKnife.git
cd ~/catkin_ws && catkin_make
```

## Steps to Build package
1. Create Catkin Workspace
```
cd ~/catkin_ws
catkin_make clean && catkin_make
```
2. Copy the repository in src folder of catkin workspace
```
git clone --recursive https://github.com/Sameep2808/gas.git
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
