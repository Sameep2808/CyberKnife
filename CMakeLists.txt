cmake_minimum_required(VERSION 2.8.3)

project(finale)
add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  move_base_msgs
  roscpp
  rospy
  std_msgs
)

generate_messages(
  DEPENDENCIES
  geometry_msgs  move_base_msgs std_msgs
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

add_executable(detect src/detect.cpp)
target_link_libraries(detect ${catkin_LIBRARIES})

add_executable(cik src/ik.cpp)
target_link_libraries(cik ${catkin_LIBRARIES})

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
