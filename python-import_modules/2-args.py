#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_num = len(argv)
    if arg_num == 1:
        print("0 arguments.")
    elif arg_num == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(arg_num - 1))
        for i in range(1, arg_num):
            print("{:d}: {:s}".format(i, argv[i]))

