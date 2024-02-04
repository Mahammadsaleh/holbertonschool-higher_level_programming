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
        if text[i] in '.?:' or i == len(text) - 1:
            print("{}".format(full.strip()), end='')
            print("\n")
            full = ""
            counter += 1
    if counter == 0:
        print(text.strip(), end="")
