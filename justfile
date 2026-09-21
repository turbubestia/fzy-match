[windows]
set shell := ["powershell.exe", "-NoLogo", "-Command"]

default: (build "debug")

setup target="debug":
	meson setup --buildtype="{{target}}" build/meson-{{target}}

build target="debug":
    meson compile -C build/meson-{{target}}

test target="debug":
    meson test -C build/meson-{{target}}

clean target="debug":
    rm -rf build/meson-{{target}}