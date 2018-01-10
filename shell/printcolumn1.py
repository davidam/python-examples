#!/usr/bin/python

inData = open('/etc/group')

for line in inData:    
    tmpFields = line.split(':')
    print(tmpFields[0])
