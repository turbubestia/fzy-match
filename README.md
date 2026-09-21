# fzy-match
A C++ library wrapper of the popular fuzzy text selector for the terminal.

*Find the oridinal work here [fzy](https://github.com/jhawthorn/fzy).*

## Build

To build this library the next dependencies must be installed
- Visual Studio Build Tools with C++
- python
- meson
- ninja
- just

To configure and build just type
```powershell
just setup release
just build release
just test release
```

### Copy Recommended VSCode Settings

To align your VSCode settings with the project's recommended configuration:

1. Navigate to the `.vscode` directory at the root of the project.
2. Copy the `settings.sample.json` file and rename the copy to `settings.json`.
3. If desired, customize the `settings.json` with your personal preferences.