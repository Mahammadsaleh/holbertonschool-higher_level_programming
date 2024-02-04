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
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            if not counter == 0:
                print("{}".format(full[1:]), end='')
            else:
                print("{}".format(full), end='')
            print()
            print()
            full = ""
            counter += 1
    if counter == 0:
        print(text, end="")
