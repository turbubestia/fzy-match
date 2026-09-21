

cc = meson.get_compiler('c')


c_args = ['-DMATCH_VERSION=1.1']
if cc.get_id() == 'msvc'
  c_args += '/w'
else
  c_args += ['-w', '-D_GNU_SOURCE']
endif


fzy_lib = static_library('fzy',
  'match.c',
  c_args: c_args,
  override_options: ['c_std=c99'],
  include_directories: include_directories('.'),
  install: true
)

install_headers('match.h', subdir: 'fzy')

fzy_dep = declare_dependency(
  link_with: fzy_lib,
  include_directories: include_directories('.')
)

# Register for dependency('fzy') in main meson.build
# meson.override_dependency('fzy', fzy_dep)