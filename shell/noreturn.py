#!/usr/bin/python# -*- coding: utf-8 -*-
import subprocess

command = "ls"
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p.communicate())




