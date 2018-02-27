import os, sys

if (len(sys.argv) == 2):
    dir = sys.argv[1]
else:
    print("You must give an unique directory to make the touch")
    sys.exit()

if (not os.path.exists(dir)):
    os.makedirs(dir)
    
os.chdir(dir)
os.mknod("newfile.txt")
os.chdir("..")
