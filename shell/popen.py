#!/usr/bin/env python
import subprocess

proc = subprocess.Popen(['tail', '-500', 'mylogfile.log'], stdout=subprocess.PIPE)

for line in proc.stdout.readlines():
    print line.rstrip()
