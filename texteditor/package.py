name = "texteditor"
version = "3.36.2"
build_command = False

def commands():
	import os
	global alias
	
	if os.name == "posix":
		alias("texteditor", r"gedit")
	elif os.name == "nt":
		alias("texteditor", r"notepad")

