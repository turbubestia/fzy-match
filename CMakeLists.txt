cmake_minimum_required(VERSION 3.21)

project(fzy-match 
    VERSION 0.1.0
    DESCRIPTION "A C++ library wrapper of the popular fuzzy text selector for the terminal."
    LANGUAGES C CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add custom CMake module path
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

# Library dependencies
find_package(GTest CONFIG REQUIRED)
find_package(fzy REQUIRED)

# Source folders
add_subdirectory(src)

# Test configuration
include(CTest)
enable_testing()
add_subdirectory(tests)
