#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    my_list = list(map(lambda x: (number) * x, my_list))
    return my_list
