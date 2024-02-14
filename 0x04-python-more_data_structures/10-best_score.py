#!/usr/bin/python3
"""
Function that returns the biggest score
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_k = None
    max_v = float('-inf')
    for k, v in a_dictionary.items():
        if v > max_v:
            max_k = k
            max_v = v

    return max_k
