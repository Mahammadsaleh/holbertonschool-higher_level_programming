#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            str += s
    return str
