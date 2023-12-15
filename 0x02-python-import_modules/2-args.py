#!/usr/bin/python3

if __name__ == "__main__":
    """the number of and list of arguments"""

    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        # while argv[0] <= n:
        print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
