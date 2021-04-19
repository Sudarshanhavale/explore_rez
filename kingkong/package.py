name = "kingkong"
version = "1.0.3"
build_command = "python {root}/install.py"

_data = {
	"label": "King Kong",
	"icon": "{root}/resources/icon.png",
}

requires = [
	"python-2.7,<4",
	"~blender==2.92.0",
	"~texteditor==1.0.0"
]

