cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(netcdf-cxx4 CONFIG REQUIRED)

add_executable(example-write src/simple_xy_wr.cpp)
target_link_libraries(example-write netcdf-cxx4::netcdf-cxx4)

add_executable(example-read src/simple_xy_rd.cpp)
target_link_libraries(example-read netcdf-cxx4::netcdf-cxx4)
