#!/usr/bin/env python
import subprocess
import sys

if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    print(arg1)
    subprocess.call(str(arg1), shell=True)
else:
    print("You must give a command to execute")
