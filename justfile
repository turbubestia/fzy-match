[windows]
set shell := ["powershell.exe", "-NoLogo", "-Command"]

default: (build "release")

setup target="release":
	meson setup --buildtype="{{target}}" build/meson-{{target}}

build target="release":
    meson compile -C build/meson-{{target}}

test target *args:
    meson test -C build/meson-{{target}} {{args}}

install target="release":
    meson install -C build/meson-{{target}} --destdir="$PWD/dist/{{target}}"

clean target="release":
    rm -rf build/meson-{{target}}