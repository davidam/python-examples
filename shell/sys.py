import sys

#f = sys.stdin
# If you need to open a file instead:
f = open('/etc/group')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    print(fields[0])
#    print(fields[2])
