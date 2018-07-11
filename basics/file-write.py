#!/usr/bin/python
# -*- coding: utf-8 -*-

file = open("testfile.txt", "w")

file.write("This is a test\n")
file.write("To add more lines.\n")
lines_of_text = ["One line of text here\n", "and another line here\n", "and yet another here\n", "and so on and so forth\n"]
file.writelines(lines_of_text)
file.close()
