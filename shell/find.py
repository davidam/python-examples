import subprocess
import os

#os.chdir("..")
 
# Set up find command
findCMD = 'find . -name "*.pyc" -exec rm {} \;'
out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# Get standard out and error
(stdout, stderr) = out.communicate()
 
# Save found files to list
filelist = stdout.decode().split()
#print(filelist)
