#!/usr/bin/python3
if __name == "__main__":
    import sys
for args in range(len(sys.argv)):
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(args))
        for i in range(args):
            print("{[}: {}".format(i + 1, sys.argv[i + 1]))
