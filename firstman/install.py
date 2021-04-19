# This script is called on `rez build`
import os
import shutil

print("Running install.py...")
root = os.path.dirname(__file__)
build_dir = os.environ["REZ_BUILD_PATH"]
install_dir = os.environ["REZ_BUILD_INSTALL_PATH"]
dirs = ["resources", "python"]

print("Copying payload to %s.." % build_dir)
for dirname in dirs:
    shutil.copytree(
        os.path.join(root, dirname),
        os.path.join(build_dir, dirname),
        ignore=shutil.ignore_patterns("*.pyc", "__pycache__")
    )

if int(os.getenv("REZ_BUILD_INSTALL")):
    
    # This part is called with `rez build --install`
    print("Installing payload to %s..." % install_dir)
    
    for dirname in dirs:
        shutil.copytree(
            os.path.join(build_dir, dirname),
            os.path.join(install_dir, dirname),
        )
