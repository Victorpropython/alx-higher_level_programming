#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Function To add all Uniq Numbers
    """
    theList = set(my_list)
    return sum(theList)
