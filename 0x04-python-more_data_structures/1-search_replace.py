#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ To replace all Occurrences of
    an element by another in a new list
    """
    return [replace if search == x else x for x in my_list]
