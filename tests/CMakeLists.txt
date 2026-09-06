
# Register tests with CTest + VS Code Test Explorer integration.
include(${CMAKE_SOURCE_DIR}/cmake/gtest_add_test.cmake)

gtest_add_test(SOURCE fzy_test.cpp PREFIX fzy_match)

# Coverage support (requires gcovr + LLVM coverage tools)
# Change to use moden msvc coverage tools if needed
option(BUILD_COVERAGE "Enable code coverage instrumentation" OFF)
if(BUILD_COVERAGE)
    target_link_options(fzy_match_fzy_test PUBLIC /PROFILE)
endif()