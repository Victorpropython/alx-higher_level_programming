#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num_arg = 0
    for i in range(len(sys.argv) - 1):
        num_arg = num_arg + int(sys.argv[i + 1])
    print("{}".format(num_arg))
