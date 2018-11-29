
import simplejson
f = open('/tmp/output.txt', 'w')
l1 = [[1, 2, 3, 4],2,3,4]
l2 = [1, 2, 3, 4]
simplejson.dump(l1, f)
f.close()

i = 0
line = ""
while (i < (len(l2) -1)):
    line = line + str(l2[i]) + ", "
    i = i +1
line = line + str(l2[i])
f2 = open('/tmp/output2.txt', 'w')
f2.write(line)
f2.close()
