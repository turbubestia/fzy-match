
gtest_dep = dependency('gtest', 
  main: true, 
  required: true, 
  fallback: ['gtest', 'gtest_dep']
)

python = import('python').find_installation()
discover_script = meson.project_source_root() / 'scripts/discover_tests.py'

res = run_command(python, discover_script, meson.current_source_dir(), check: true)
raw_output = res.stdout().strip()

if raw_output != ''
  lines = raw_output.split('\n')
  created_exes = {}

  foreach line : lines
    parts = line.split(':')
    file_name = parts[0]
    test_case = parts[1]
    line_number = parts[2]
    
    # Target executable name (e.g. fzy_test.cpp -> fzy_test)
    exe_name = file_name.replace('.cpp', '')

    # Instantiate the target executable once per file
    if not created_exes.has_key(exe_name)
      exe = executable(exe_name, file_name, dependencies: [gtest_dep, fzy_match_dep] )
      created_exes += {exe_name: exe}
    else
      exe = created_exes[exe_name]
    endif

    # Register individual GTest case with gtest protocol
    test(test_case,
      exe,
      args: ['--gtest_filter=' + test_case],
      protocol: 'gtest'
    )
  endforeach
endif