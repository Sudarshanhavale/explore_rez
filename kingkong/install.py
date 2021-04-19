# This script will be called on "rez build"

import os
import shutil

print("Runnig install.py...")
root = os.path.dirname(__file__)
build_dir = os.environ["REZ_BUILD_PATH"]
install_dir = os.environ["REZ_BUILD_INSTALL_PATH"]


print("Coping payloads to {}...".format(build_dir))
shutil.copytree(
	os.path.join(root, "resources"),
	os.path.join(build_dir, "resources"),
	ignore = shutil.ignore_patterns("*.pyc", "__pycache__")
)

if int(os.getenv("REZ_BUILD_INSTALL")):
	# This part is called with "rez build --install"
	print("Installing payloads to {}".format(install_dir))
	shutil.copytree(
		os.path.join(build_dir, "resources"),
		os.path.join(install_dir, "resources"),
	)

