#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    args = len(argv)
    if args == 0:
        print("0")
    elif args == 1:
        print("{}".format(int(argv[1])))
    else:
        for i in range(1, args):
            result += int(argv[i])
        print("{:d}".format(result))
