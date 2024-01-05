#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """To replace an element in a position"""
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    else:
        my_list[idx] = element
    return (my_list)
