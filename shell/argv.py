#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # The first argument of sys.argv is always the filename,
    # meaning that the length of system arguments will be
    # more than one, when command-line arguments exist.
    if len(sys.argv) > 2:
            num1 = long(sys.argv[1])
            num2 = long(sys.argv[2])
    else:
            print("This command takes two arguments and adds them")
            print("Less than two arguments given.")
            sys.exit(1)
    print("%s" % str(num1 + num2))
