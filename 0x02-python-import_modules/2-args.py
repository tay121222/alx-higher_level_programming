#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    if length == 1:
        print("{:d} arguments.".format(length - 1))
    elif length > 1:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
