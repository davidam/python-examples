
import simplejson
f = open('/tmp/output.txt', 'w')
simplejson.dump([[1, 2, 3, 4],2,3,4], f)
f.close()
