name = "firstman"
version = "1.0.2"
build_command = "python {root}/install.py"

# Define arbitrary data, label and icon are understandable by allzpark.
_data = {
	"label": "First Man",
	"icon": "{root}/resources/icon.png",
}

# Define all requires of type packages and applications.
requires = [
	"python-2.7,<4",
	"~blender==2.92.0",
	"~texteditor==1.0.0",
]


# Define required envs to be called inside application.
def commands():
	global env
	
	env["PROJECT_NAME"] = "firstman"
	env["PROJECT_FRAMERATE"] = "25"
	env["PROJECT_TAGS"] = "awesome,great"
	
	env["PYTHONPATH"].prepend("{root}/python")

