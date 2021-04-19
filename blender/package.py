name = "blender"
version = "2.92.0"
build_command = False

_data = {
    "icon": "{root}/resources/icon.png"
}

# requires = ['rezutil-1',]


def commands():
    global alias
    import os

    if os.name == "posix":
        alias("blender", r"blender")
