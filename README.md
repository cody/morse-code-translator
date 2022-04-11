# morse-code-translator
a simple morse code translator using python/tkinter

This program's primary purpose is to serve as a learning exercise for me in trying to become more comfortable with Python/Tkinter.

# Functions
- English to Morse
- Morse to English
- Play audio of the translated morse code
- Show a visual morse code chart in a new window

# Issues
This app is mostly functional, but Tkinter has some weird quirks on MacOS which is the OS I'm currently using for dev learning. For example, Tkinter on MacOS doesn't like to use relative file paths even though Windows and Linux seems to have no issue. Because of this, I've had to include some of the files using an absolute path. I'm currently trying to research why this is happening, and trying to determine whether it's my ENV or rather an OS limitation (which I doubt it is).
