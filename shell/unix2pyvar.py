import os
f = os.popen('date')
now = f.read()
print("Today is ", now)
