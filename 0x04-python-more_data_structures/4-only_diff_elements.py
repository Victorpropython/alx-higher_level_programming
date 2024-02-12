#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
     function to return a set of
     all element present in only one set
     """
    a = set_1
    b = set_2
    return (set(a ^ b))
