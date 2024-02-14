#!/usr/bin/python3
def roman_to_int(roman_string):
    if not 'str' | None in roman_string:
        return 0
    
    new_dict = {'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,
            'D' : 500,'M' : 1000}
    for k, v in new_dict.items():
        if v in roman_string:
            return v
