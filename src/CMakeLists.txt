
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

add_library(fzy_match STATIC)

target_include_directories(fzy_match PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

target_sources(fzy_match PRIVATE
    fzy.cpp
)

target_sources(fzy_match PUBLIC FILE_SET HEADERS FILES
    fzy.hpp
)

target_link_libraries(fzy_match PRIVATE fzy)

# Debug-only test-path override: only active when SETTINGS_DEBUG_TEST_PATH cache variable is set.
if(SETTINGS_DEBUG_TEST_PATH)
    target_compile_definitions(fzy_match PUBLIC SETTINGS_DEBUG_TEST_PATH)
endif()

install(TARGETS fzy_match EXPORT fzy_matchTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    FILE_SET HEADERS DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(FILES fzy.hpp DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# Export configuration
install(EXPORT fzy_matchTargets
    FILE fzy_matchTargets.cmake
    NAMESPACE turbubestia::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/turbubestia/cmake
)

# Package
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
  "${CMAKE_CURRENT_BINARY_DIR}/fzy_matchConfig.cmake"
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/turbubestia/cmake
)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/fzy_matchConfigVersion.cmake"
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY SameMajorVersion
)

install(FILES
          "${CMAKE_CURRENT_BINARY_DIR}/fzy_matchConfig.cmake"
          "${CMAKE_CURRENT_BINARY_DIR}/fzy_matchConfigVersion.cmake"
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/turbubestia/cmake
)