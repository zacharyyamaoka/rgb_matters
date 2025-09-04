cmake_minimum_required(VERSION 3.5)
project(rgb_matters)

find_package(ament_cmake REQUIRED)

# Install the Python package as-is
ament_python_install_package(${PROJECT_NAME})

ament_package()