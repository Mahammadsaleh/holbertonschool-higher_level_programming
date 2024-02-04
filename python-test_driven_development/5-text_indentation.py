#!/usr/bin/python3
"""documentaion"""


def text_indentation(text):
    """Text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    full = ""
    counter = 0
    for i in range(len(text)):
        full += text[i]
        if text[i] in '.?:':
            print("{}".format(full.strip()), end='')
            if i != len(text) - 1 or text[i] not in '.?:':
                print("\n")
            full = ""
            counter += 1
    if counter == 0 or full:
        print(full.strip(), end="")
