#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
                char = chr(ord(str[i]) - 32)
                print("{:s}".format(char), end="")
        else:
            print("{:s}".format(str[i]), end="")
    print("")
