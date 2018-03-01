from time import gmtime, strftime

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

import time
print(time.strptime("30 Nov 00", "%d %b %y"))
print(time.time())
