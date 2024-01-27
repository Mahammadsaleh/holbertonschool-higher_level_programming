#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            res += chr(ord(i) - 32)
        elif 65 <= ord(i) <= 90:
            res += i
        elif i.isdigit() or i.isspace():
            res += i
    print("{}".format(res))
