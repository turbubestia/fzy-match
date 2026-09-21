
subdir('fzy')

# 1. Define the include directory object
fzy_match_inc = include_directories('.')

# 2. Build the static library
fzy_match_lib = static_library('fzy_match',
  'fzy.cpp',
  dependencies: fzy_dep,
  include_directories: fzy_match_inc,
  install: true
)

# 3. EXPOSE THE DEPENDENCY TO TESTS/CONSUMERS
fzy_match_dep = declare_dependency(
  link_with: fzy_match_lib,
  include_directories: fzy_match_inc,
  dependencies: fzy_dep # Forwards thirdparty fzy dependency automatically
)