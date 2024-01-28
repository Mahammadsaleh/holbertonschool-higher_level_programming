#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    for index in range(1, len(argv)):
        result += int(argv[index])
    print("{}".format(result))
