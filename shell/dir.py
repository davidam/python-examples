import os

if os.path.exists("/tmp/"):
    print("The temporal directory exists")

if os.path.isdir("/tmp/"):
    print("tmp is a directory")
    
if os.path.ismount("/tmp/"):
    print("tmp is mounted")
