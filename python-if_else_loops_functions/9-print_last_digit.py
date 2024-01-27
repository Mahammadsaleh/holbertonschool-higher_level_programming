#!/usr/bin/python3
def print_last_digit(number):
    rest = abs(number) % 10
    print("{}".format(rest), end="")
    return (rest)
