cmake_minimum_required(VERSION 3.17)
set(CMAKE_C_STANDARD 11)
set(PROJECT_NAME cpython_std_algorithm)
project(${PROJECT_NAME} C)
# This path contains python headers like Python.h
include_directories("/usr/include/python3.8")
add_library(${PROJECT_NAME} SHARED src/init.c src/libstd.c)
# Set output dir to 'lib/' in the project root
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)
# Changing output name to std.so, because it dictates how you import it to python
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME "std")