#!/usr/bin/python3
"""
    to print a dictionary by ordered keys
"""
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for m in a:
        print("{}: {}".format(m, a_dictionary[m]))
