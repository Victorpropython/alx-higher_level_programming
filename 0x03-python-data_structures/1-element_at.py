#!/usr/bin/python3

def element_at(my_list, idx):
    """To retrieve an element @ feom a list in c"""
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
