name = "texteditor"
version = "1.0.0"
build_command = False

def commands():
    import os
    global alias

    if os.name == "nt":
        alias("texteditor", r"notepad")
    elif os.name == "darwin":
        alias("texteditor", r"textedit")
    else:
        alias("texteditor", r"gedit")
