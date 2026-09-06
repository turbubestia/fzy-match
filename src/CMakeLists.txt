add_library(fzy_match STATIC)

target_include_directories(fzy_match PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(fzy_match PUBLIC fzy )

set_target_properties(fzy_match PROPERTIES
    CXX_STANDARD 20
    CXX_STANDARD_REQUIRED ON
)

# Debug-only test-path override: only active when SETTINGS_DEBUG_TEST_PATH cache variable is set.
if(SETTINGS_DEBUG_TEST_PATH)
    target_compile_definitions(fzy_match PUBLIC SETTINGS_DEBUG_TEST_PATH)
endif()

target_sources(fzy_match PRIVATE
    fzy.hpp
    fzy.cpp
)
