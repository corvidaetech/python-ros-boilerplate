cmake_minimum_required(VERSION 2.8.3)
project(sample_node)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

catkin_package(
#  INCLUDE_DIRS include
#  CATKIN_DEPENDS std_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME} python/sample_node.py)
#target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})
